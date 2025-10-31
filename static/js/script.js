// Menu mobile
const burger = document.querySelector('.burger');
const nav = document.querySelector('.nav-links');

burger.addEventListener('click', () => {
    nav.classList.toggle('active');
    burger.classList.toggle('active');
});

// Fermer les messages flash
document.querySelectorAll('.close-flash').forEach(btn => {
    btn.addEventListener('click', function() {
        this.parentElement.style.animation = 'slideOut 0.3s ease-out';
        setTimeout(() => this.parentElement.remove(), 300);
    });
});

// Auto-fermeture des messages flash après 5 secondes
setTimeout(() => {
    document.querySelectorAll('.flash').forEach(flash => {
        flash.style.animation = 'slideOut 0.3s ease-out';
        setTimeout(() => flash.remove(), 300);
    });
}, 5000); 



// ============================================
// ACCORDÉON POUR LA PAGE À PROPOS
// À ajouter à la fin de script.js
// ============================================

// Gestion de l'accordéon
document.addEventListener('DOMContentLoaded', function() {
    const accordionHeaders = document.querySelectorAll('.accordion-header');
    
    accordionHeaders.forEach(header => {
        header.addEventListener('click', function() {
            const accordionItem = this.parentElement;
            const accordionContent = accordionItem.querySelector('.accordion-content');
            const accordionIcon = accordionItem.querySelector('.accordion-icon');
            
            // Fermer tous les autres accordéons (optionnel)
            // Commentez ces lignes si vous voulez que plusieurs sections restent ouvertes
            /*
            document.querySelectorAll('.accordion-item').forEach(item => {
                if (item !== accordionItem && item.classList.contains('active')) {
                    item.classList.remove('active');
                    item.querySelector('.accordion-content').style.display = 'none';
                    item.querySelector('.accordion-icon').textContent = '+';
                }
            });
            */
            
            // Toggle de l'accordéon actuel
            accordionItem.classList.toggle('active');
            
            if (accordionContent.style.display === 'block') {
                accordionContent.style.display = 'none';
                accordionIcon.textContent = '+';
            } else {
                accordionContent.style.display = 'block';
                accordionIcon.textContent = '-';
            }
        });
    });

    // Animation des barres de compétences au scroll
    const observerOptions = {
        threshold: 0.5
    };

    const observer = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const skillBars = entry.target.querySelectorAll('.skill-progress-bar');
                skillBars.forEach(bar => {
                    bar.style.animation = 'fillBar 1.5s ease-out';
                });
            }
        });
    }, observerOptions);

    const skillsSection = document.querySelector('.skills-detailed');
    if (skillsSection) {
        observer.observe(skillsSection);
    }
});