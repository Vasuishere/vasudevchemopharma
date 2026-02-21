/**
 * Vasudev Chemo Pharma – Global site JavaScript
 * Mobile-first, null-safe, no duplicated logic.
 *
 * Page-specific scripts (hero slider, tabs, category filter, etc.)
 * live inside each template's {% block extra_js %}.
 */
document.addEventListener('DOMContentLoaded', function () {

    /* ─── Smooth scrolling for anchor links ─── */
    document.querySelectorAll('a[href^="#"]').forEach(function (anchor) {
        anchor.addEventListener('click', function (e) {
            var href = this.getAttribute('href');
            if (href === '#') return;
            var target = href.startsWith('#') ? document.getElementById(href.substring(1)) : document.querySelector(href);
            if (target) {
                e.preventDefault();
                var headerHeight = 0;
                var header = document.querySelector('header');
                if (header) headerHeight = header.offsetHeight;
                var targetPosition = target.offsetTop - headerHeight - 20;
                window.scrollTo({ top: targetPosition, behavior: 'smooth' });
            }
        });
    });

    /* ─── Contact form handling (only on pages with #contactForm) ─── */
    var contactForm = document.getElementById('contactForm');
    if (contactForm) {
        contactForm.addEventListener('submit', function (e) {
            e.preventDefault();

            var formData = new FormData(contactForm);
            var name = formData.get('name');
            var email = formData.get('email');
            var message = formData.get('message');

            if (!name || !email || !message) {
                alert('Please fill in all required fields (Name, Email, and Message).');
                return;
            }

            var emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
            if (!emailRegex.test(email)) {
                alert('Please enter a valid email address.');
                return;
            }

            var submitBtn = contactForm.querySelector('.submit-btn');
            if (!submitBtn) return;
            var originalText = submitBtn.textContent;
            submitBtn.classList.add('loading');
            submitBtn.textContent = 'Sending...';
            submitBtn.disabled = true;

            // Simulated submission – swap for real API call in production
            setTimeout(function () {
                submitBtn.classList.remove('loading');
                submitBtn.textContent = originalText;
                submitBtn.disabled = false;
                showSuccessMessage('Thank you for your inquiry! We will get back to you within 24 hours.');
                contactForm.reset();
            }, 2000);
        });

        function showSuccessMessage(msg) {
            var el = document.querySelector('.success-message');
            if (!el) {
                el = document.createElement('div');
                el.className = 'success-message';
                contactForm.parentNode.insertBefore(el, contactForm);
            }
            el.textContent = msg;
            el.classList.add('show');
            setTimeout(function () { el.classList.remove('show'); }, 5000);
        }
    }

    /* ─── Scroll-triggered fade-in animations ─── */
    if (window.IntersectionObserver) {
        var observerOptions = { threshold: 0.1, rootMargin: '0px 0px -50px 0px' };
        var observer = new IntersectionObserver(function (entries) {
            entries.forEach(function (entry) {
                if (entry.isIntersecting) {
                    entry.target.classList.add('visible');
                }
            });
        }, observerOptions);

        var animateSelectors = '.product-card, .certificate, .partner, .about-text, .contact-info, .service-card, .mvv-card, .feature-item, .stat-item';
        document.querySelectorAll(animateSelectors).forEach(function (el) {
            el.classList.add('fade-in');
            observer.observe(el);
        });
    }

    /* ─── Form field focus micro-interaction ─── */
    document.querySelectorAll('.form-group input, .form-group textarea, .form-group select').forEach(function (field) {
        field.addEventListener('focus', function () {
            this.parentElement.style.transform = 'scale(1.02)';
            this.parentElement.style.transition = 'transform 0.2s ease';
        });
        field.addEventListener('blur', function () {
            this.parentElement.style.transform = 'scale(1)';
        });
    });

    /* ─── Partners auto-scroll duplication (seamless loop) ─── */
    var partnersGrid = document.querySelector('.partners-grid');
    if (partnersGrid && partnersGrid.children.length > 0) {
        var originals = Array.from(partnersGrid.children);
        originals.forEach(function (node) {
            var clone = node.cloneNode(true);
            clone.setAttribute('aria-hidden', 'true');
            clone.removeAttribute('id');
            // Prevent duplicated focusable elements from tab order
            clone.querySelectorAll('a, button, input, [tabindex]').forEach(function (el) {
                el.setAttribute('tabindex', '-1');
            });
            partnersGrid.appendChild(clone);
        });
    }

    /* ─── Partners pause / play toggle ─── */
    var pauseBtn = document.querySelector('.partners-pause-btn');
    if (pauseBtn) {
        pauseBtn.addEventListener('click', function () {
            var track = document.querySelector(pauseBtn.getAttribute('aria-controls'));
            if (!track) track = pauseBtn.closest('.partners-track-wrapper');
            if (!track) return;
            var target = track.querySelector('.partners-track') || track.querySelector('.partners-grid') || track;
            var isPaused = getComputedStyle(target).animationPlayState === 'paused';
            target.style.animationPlayState = isPaused ? 'running' : 'paused';
            pauseBtn.setAttribute('aria-pressed', isPaused ? 'false' : 'true');
            pauseBtn.textContent = isPaused ? '❚❚ Pause' : '▶ Play';
        });
    }

    /* ─── Dynamic footer year ─── */
    var currentYear = new Date().getFullYear();
    document.querySelectorAll('.footer-section p').forEach(function (el) {
        var text = el.textContent;
        // Replace any 4-digit year (2020-2099) so it never goes stale
        if (/\b20\d{2}\b/.test(text)) {
            el.textContent = text.replace(/\b20\d{2}\b/, currentYear);
        }
    });

     /* ─── Header scroll behavior (as requested) ───
         Scroll down => hide navbar
         Scroll up   => show navbar
     */
    var pageHeader = document.querySelector('header');
    if (pageHeader) {
        var lastScrollTop = window.pageYOffset || document.documentElement.scrollTop || 0;
        var ticking = false;
        var minDelta = 8;

        function updateHeaderVisibility() {
            var currentScrollTop = window.pageYOffset || document.documentElement.scrollTop || 0;
            var delta = currentScrollTop - lastScrollTop;

            if (Math.abs(delta) < minDelta) {
                ticking = false;
                return;
            }

            if (currentScrollTop <= 10) {
                pageHeader.classList.remove('header-hidden');
            } else if (delta > 0) {
                pageHeader.classList.add('header-hidden');
            } else {
                pageHeader.classList.remove('header-hidden');
            }

            lastScrollTop = currentScrollTop;
            ticking = false;
        }

        window.addEventListener('scroll', function () {
            if (!ticking) {
                window.requestAnimationFrame(updateHeaderVisibility);
                ticking = true;
            }
        }, { passive: true });
    }
});
