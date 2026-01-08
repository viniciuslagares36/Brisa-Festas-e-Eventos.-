// Elementos do DOM
const openModalBtn = document.getElementById('openModal');
const closeModalBtn = document.getElementById('closeModal');
const modalOverlay = document.getElementById('modalOverlay');
const newsletterForm = document.getElementById('newsletterForm');
const formContent = document.getElementById('formContent');
const successContent = document.getElementById('successContent');
const submitBtn = document.getElementById('submitBtn');
const btnText = submitBtn.querySelector('.btn-text');
const btnLoading = submitBtn.querySelector('.btn-loading');

// Abrir modal
openModalBtn.addEventListener('click', () => {
  modalOverlay.classList.add('active');
});

// Fechar modal
closeModalBtn.addEventListener('click', closeModal);

// Fechar modal clicando fora
modalOverlay.addEventListener('click', (e) => {
  if (e.target === modalOverlay) {
    closeModal();
  }
});

// Fechar com tecla ESC
document.addEventListener('keydown', (e) => {
  if (e.key === 'Escape') {
    closeModal();
  }
});

function closeModal() {
  modalOverlay.classList.remove('active');
  
  // Resetar formulário após fechar (com delay para animação)
  setTimeout(() => {
    formContent.style.display = 'block';
    successContent.style.display = 'none';
    newsletterForm.reset();
  }, 300);
}

// Enviar formulário
newsletterForm.addEventListener('submit', async (e) => {
  e.preventDefault();
  
  const name = document.getElementById('name').value;
  const email = document.getElementById('email').value;
  
  // Mostrar loading
  submitBtn.disabled = true;
  btnText.style.display = 'none';
  btnLoading.style.display = 'inline';
  
  try {
    // Enviar para o backend Python
    const response = await fetch('/api/newsletter', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ name, email }),
    });
    
    if (response.ok) {
      showSuccess();
    } else {
      throw new Error('Erro ao cadastrar');
    }
  } catch (error) {
    // Para teste sem backend, simular sucesso
    console.log('Dados do formulário:', { name, email });
    
    // Simular delay de rede
    await new Promise(resolve => setTimeout(resolve, 1000));
    showSuccess();
  }
});

function showSuccess() {
  // Esconder formulário e mostrar sucesso
  formContent.style.display = 'none';
  successContent.style.display = 'block';
  
  // Resetar botão
  submitBtn.disabled = false;
  btnText.style.display = 'inline';
  btnLoading.style.display = 'none';
  
  // Fechar automaticamente após 3 segundos
  setTimeout(() => {
    closeModal();
  }, 3000);
}
 // ==================== MOBILE MENU ====================
        const mobileMenuBtn = document.getElementById('mobileMenuBtn');
        const navMenu = document.getElementById('navMenu');

        mobileMenuBtn.addEventListener('click', () => {
            navMenu.classList.toggle('active');
        });

        // Close menu when clicking a link
        document.querySelectorAll('.nav-link').forEach(link => {
            link.addEventListener('click', () => {
                navMenu.classList.remove('active');
            });
        });

        // ==================== HEADER SCROLL ====================
        const header = document.getElementById('header');

        window.addEventListener('scroll', () => {
            if (window.scrollY > 100) {
                header.classList.add('scrolled');
            } else {
                header.classList.remove('scrolled');
            }
        });

        // ==================== SMOOTH SCROLL ====================
        document.querySelectorAll('a[href^="#"]').forEach(anchor => {
            anchor.addEventListener('click', function (e) {
                e.preventDefault();
                const target = document.querySelector(this.getAttribute('href'));
                if (target) {
                    target.scrollIntoView({
                        behavior: 'smooth',
                        block: 'start'
                    });
                }
            });
        });

        // ==================== FADE IN ON SCROLL ====================
        const fadeElements = document.querySelectorAll('.fade-in');

        const fadeObserver = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('visible');
                }
            });
        }, {
            threshold: 0.1,
            rootMargin: '0px 0px -50px 0px'
        });

        fadeElements.forEach(el => fadeObserver.observe(el));

        // ==================== CONFETTI EFFECT ====================
        function createConfetti(e) {
            const button = e.currentTarget;
            const rect = button.getBoundingClientRect();
            const colors = ['#E91E8C', '#2ECC71', '#F1C40F', '#3498DB', '#9B59B6'];

            for (let i = 0; i < 15; i++) {
                const confetti = document.createElement('div');
                confetti.style.cssText = `
                    position: fixed;
                    width: 10px;
                    height: 10px;
                    background: ${colors[Math.floor(Math.random() * colors.length)]};
                    border-radius: ${Math.random() > 0.5 ? '50%' : '0'};
                    pointer-events: none;
                    z-index: 9999;
                    left: ${rect.left + rect.width / 2}px;
                    top: ${rect.top + rect.height / 2}px;
                `;
                document.body.appendChild(confetti);

                const angle = (Math.random() * 360) * (Math.PI / 180);
                const velocity = 5 + Math.random() * 5;
                const vx = Math.cos(angle) * velocity;
                const vy = Math.sin(angle) * velocity;

                let x = 0, y = 0, opacity = 1;

                function animate() {
                    x += vx;
                    y += vy + 2;
                    opacity -= 0.02;

                    confetti.style.transform = `translate(${x}px, ${y}px) rotate(${x * 5}deg)`;
                    confetti.style.opacity = opacity;

                    if (opacity > 0) {
                        requestAnimationFrame(animate);
                    } else {
                        confetti.remove();
                    }
                }

                setTimeout(() => animate(), i * 30);
            }
        }

        document.querySelectorAll('.btn-confetti').forEach(btn => {
            btn.addEventListener('click', createConfetti);
        });

        // ==================== FORM SUBMISSION ====================
        const contactForm = document.getElementById('contactForm');

        contactForm.addEventListener('submit', (e) => {
            e.preventDefault();

            const formData = new FormData(contactForm);
            const name = formData.get('name');
            const phone = formData.get('phone');
            const event = formData.get('event');
            const message = formData.get('message');
            console.log('Form Data:', { name, phone, event, message });
        });
