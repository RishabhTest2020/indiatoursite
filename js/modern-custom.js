document.addEventListener('DOMContentLoaded', function() {
    "use strict";

    /* ==========================================================================
       1. THEME SWITCHER LOGIC
       ========================================================================== */
    const body = document.body;
    const themeToggleBtn = document.getElementById('themeToggle');
    
    // Check local storage for theme preference
    if (localStorage.getItem('theme') === 'dark') {
        body.classList.add('dark-mode');
    }

    if (themeToggleBtn) {
        themeToggleBtn.addEventListener('click', function() {
            body.classList.toggle('dark-mode');
            
            // Save preference to local storage
            if (body.classList.contains('dark-mode')) {
                localStorage.setItem('theme', 'dark');
            } else {
                localStorage.setItem('theme', 'light');
            }
        });
    }

    /* ==========================================================================
       2. ISOTOPE CUSTOM FILTER FOR SEARCH CONSOLE
       ========================================================================== */
    const searchBtn = document.getElementById('searchSubmit');
    if (searchBtn) {
        searchBtn.addEventListener('click', function(e) {
            e.preventDefault();
            
            // Perform filtering
            if (window.jQuery && jQuery.fn.isotope) {
                const $ = window.jQuery;
                $('.grid').isotope({
                    filter: function() {
                        const name = $(this).find('h4, h5').text().toLowerCase();
                        const state = $(this).find('.cat').text().toLowerCase();
                        
                        // Text Search
                        const searchVal = $('#searchDest').val().trim().toLowerCase();
                        const matchesSearch = !searchVal || name.includes(searchVal) || state.includes(searchVal);
                        
                        // Vibe Select
                        const selectedVibe = $('#searchVibe').val();
                        const cardVibe = $(this).attr('data-vibe') || '';
                        const matchesVibe = !selectedVibe || selectedVibe === 'all' || cardVibe === selectedVibe;
                        
                        // Region Select
                        const selectedRegion = $('#searchRegion').val();
                        const matchesRegion = !selectedRegion || selectedRegion === 'all' || $(this).hasClass(selectedRegion);
                        
                        return matchesSearch && matchesVibe && matchesRegion;
                    }
                });

                // Scroll to portfolio
                const portfolioSec = document.getElementById('middle');
                if (portfolioSec) {
                    portfolioSec.scrollIntoView({ behavior: 'smooth', block: 'start' });
                }

                // Visual Feedback on Search button
                const originalContent = searchBtn.innerHTML;
                searchBtn.innerHTML = '<i class="fa fa-circle-o-notch fa-spin"></i> Finding...';
                setTimeout(() => {
                    searchBtn.innerHTML = originalContent;
                }, 1000);
            }
        });
    }

    /* ==========================================================================
       3. INTERACTIVE VIBE PLANNER
       ========================================================================== */
    const vibeCards = document.querySelectorAll('.vibe-card');
    const vibeRecommendations = document.querySelector('.vibe-recommendations');
    const recVibeTitle = document.getElementById('recVibeTitle');
    const recVibeDesc = document.getElementById('recVibeDesc');
    const viewVibeToursBtn = document.getElementById('viewVibeTours');

    const vibeData = {
        adventure: {
            title: "Mountain & Adventure Expeditions",
            desc: "Feel the rush of adrenaline in India's most rugged terrains! Experience standard-setting camel safaris in the golden deserts of Rajasthan, go river rafting in the clean currents of Meghalaya's Umngot, or trek the breathtaking mountain passes of Himachal and Jammu & Kashmir. Ideal for travelers looking to test their limits.",
            filter: "adventure"
        },
        culture: {
            title: "Cultural & Heritage Pathways",
            desc: "Unravel thousands of years of rich history. Wander through the magnificent palaces of Udaipur, step back in time among the historic ruins of Hampi, marvel at the engineering of Gwalior Fort, and stand in awe of Punjab's serene Golden Temple. Perfect for historians, families, and architecture lovers.",
            filter: "culture"
        },
        nature: {
            title: "Pristine Nature & Wildlife",
            desc: "Escape the noise and reconnect with mother earth. Glide on a traditional houseboat along the backwaters of Alleppey, gaze into the crystal clear depths of Meghalaya's waters, or take in the dramatic landscapes of Mon and Srinagar. Formulated for peace seekers and photographers.",
            filter: "nature"
        },
        beach: {
            title: "Sun, Sand & Coastal Serenity",
            desc: "Bask in the tropical warmth of India's coastline. Stroll along the silver sands of Colva Beach in Goa, witness dramatic sunsets by the Vivekananda Rock Memorial in Tamil Nadu, or experience the tranquil coconut groves of Kerala. Built for ultimate relaxation and coastal romance.",
            filter: "beach"
        }
    };

    let selectedVibe = '';

    vibeCards.forEach(card => {
        card.addEventListener('click', function() {
            const vibe = this.getAttribute('data-vibe');
            
            // Toggle active state
            vibeCards.forEach(c => c.classList.remove('active'));
            this.classList.add('active');

            // Set content in recommendation card
            const data = vibeData[vibe];
            if (data) {
                selectedVibe = data.filter;
                recVibeTitle.textContent = data.title;
                recVibeDesc.textContent = data.desc;
                
                // Show recommendations panel
                vibeRecommendations.style.display = 'block';
                vibeRecommendations.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
                
                // Highlight matching cards visually in the portfolio
                if (window.jQuery) {
                    const $ = window.jQuery;
                    $('.single-portfolio').removeClass('highlight-card');
                    $(`.single-portfolio[data-vibe="${selectedVibe}"]`).addClass('highlight-card');
                }
            }
        });
    });

    if (viewVibeToursBtn) {
        viewVibeToursBtn.addEventListener('click', function() {
            if (selectedVibe && window.jQuery && jQuery.fn.isotope) {
                const $ = window.jQuery;
                $('.filters ul li').removeClass('active');
                
                // Filter isotope to just this vibe
                $('.grid').isotope({
                    filter: function() {
                        return $(this).attr('data-vibe') === selectedVibe;
                    }
                });

                // Scroll to portfolio
                const portfolioSec = document.getElementById('middle');
                if (portfolioSec) {
                    portfolioSec.scrollIntoView({ behavior: 'smooth', block: 'start' });
                }
            }
        });
    }

    /* ==========================================================================
       4. FLOATING INQUIRY ASSISTANT (CHATBOT)
       ========================================================================== */
    const chatFab = document.getElementById('chatFab');
    const chatPanel = document.getElementById('chatPanel');
    const chatClose = document.getElementById('chatClose');
    const chatBody = document.getElementById('chatBody');
    const chatInput = document.getElementById('chatInput');
    const chatForm = document.getElementById('chatForm');
    const badge = chatFab ? chatFab.querySelector('.chat-fab-badge') : null;

    if (chatFab && chatPanel && chatClose) {
        chatFab.addEventListener('click', function() {
            chatPanel.classList.toggle('open');
            if (badge) badge.style.display = 'none'; // Clear notification when clicked
            scrollToBottom();
        });

        chatClose.addEventListener('click', function() {
            chatPanel.classList.remove('open');
        });
    }

    function scrollToBottom() {
        if (chatBody) {
            chatBody.scrollTop = chatBody.scrollHeight;
        }
    }

    function addMessage(sender, text, isHtml = false) {
        const msgDiv = document.createElement('div');
        msgDiv.className = `chat-msg ${sender}`;
        
        const bubble = document.createElement('div');
        bubble.className = 'chat-bubble';
        if (isHtml) {
            bubble.innerHTML = text;
        } else {
            bubble.textContent = text;
        }
        
        const time = document.createElement('span');
        time.className = 'chat-msg-time';
        const now = new Date();
        time.textContent = now.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
        
        msgDiv.appendChild(bubble);
        msgDiv.appendChild(time);
        
        if (chatBody) {
            chatBody.appendChild(msgDiv);
            scrollToBottom();
        }
    }

    // Handle bot response logic
    function botReply(userText) {
        setTimeout(() => {
            const text = userText.toLowerCase();
            if (text.includes('callback') || text.includes('call')) {
                askForCallback();
            } else if (text.includes('itinerary') || text.includes('plan') || text.includes('book')) {
                startItineraryWizard();
            } else if (text.includes('best time') || text.includes('when to visit')) {
                addMessage('bot', "Most of India is great to visit from October to March when it is cool and dry. The Himalayan region (Himachal, Kashmir) is best from April to July for summer escapes, or December to February for winter snow.");
                addQuickReplies();
            } else {
                addMessage('bot', "I can help you customize an unforgettable journey across India! What would you like to do next?");
                addQuickReplies();
            }
        }, 1000);
    }

    function addQuickReplies() {
        const div = document.createElement('div');
        div.className = 'chat-quick-replies';
        
        const options = [
            { text: "🗺️ Plan Custom Tour", action: startItineraryWizard },
            { text: "📞 Request Callback", action: askForCallback },
            { text: "🌤️ Best Time to Visit?", action: () => {
                addMessage('user', "What's the best time to visit?");
                botReply("best time");
            }}
        ];

        options.forEach(opt => {
            const chip = document.createElement('button');
            chip.className = 'chat-chip';
            chip.textContent = opt.text;
            chip.onclick = function() {
                div.remove();
                opt.action();
            };
            div.appendChild(chip);
        });

        if (chatBody) {
            chatBody.appendChild(div);
            scrollToBottom();
        }
    }

    function askForCallback() {
        addMessage('bot', "Sure! Please provide your phone number and name, and our travel expert will call you within 2 hours.");
        
        const formHtml = `
            <form class="wizard-form" id="callbackForm">
                <div>
                    <label>Your Name</label>
                    <input type="text" id="cbName" required placeholder="John Doe">
                </div>
                <div>
                    <label>Phone Number</label>
                    <input type="tel" id="cbPhone" required placeholder="+91 98765 43210">
                </div>
                <button type="submit" class="primary-btn" style="padding: 8px 16px; font-size: 13px;">Submit Request</button>
            </form>
        `;
        addMessage('bot', formHtml, true);
        
        setTimeout(() => {
            const form = document.getElementById('callbackForm');
            if (form) {
                form.onsubmit = function(e) {
                    e.preventDefault();
                    const name = document.getElementById('cbName').value;
                    const phone = document.getElementById('cbPhone').value;
                    
                    form.innerHTML = '<p style="color:var(--accent-primary);margin:0;"><i class="fa fa-spinner fa-spin"></i> Submitting request...</p>';
                    
                    // Submit to Formspree
                    const formData = new FormData();
                    formData.append('name', name);
                    formData.append('phone', phone);
                    formData.append('type', 'Callback Request');
                    
                    fetch('https://formspree.io/f/xzzgaydr', {
                        method: 'POST',
                        body: formData,
                        headers: { 'Accept': 'application/json' }
                    }).then(() => {
                        form.innerHTML = '<span style="color:#10b981;font-weight:600;"><i class="fa fa-check"></i> Request Received! We will call you shortly.</span>';
                        setTimeout(() => {
                            addMessage('bot', "Is there anything else I can assist you with today?");
                            addQuickReplies();
                        }, 1500);
                    }).catch(() => {
                        form.innerHTML = '<span style="color:#ef4444;"><i class="fa fa-times"></i> Error. Please try again.</span>';
                    });
                };
            }
        }, 100);
    }

    function startItineraryWizard() {
        addMessage('bot', "Let's plan your dream itinerary! Please fill out this quick detail sheet.");
        
        const formHtml = `
            <form class="wizard-form" id="itineraryForm">
                <div>
                    <label>Preferred Destination</label>
                    <select id="itDest">
                        <option value="kashmir">Kashmir (Himalayas)</option>
                        <option value="kerala">Kerala (Backwaters)</option>
                        <option value="rajasthan">Rajasthan (Royal Forts)</option>
                        <option value="goa">Goa (Beaches)</option>
                        <option value="golden-temple">Golden Temple & Punjab</option>
                    </select>
                </div>
                <div>
                    <label>Duration</label>
                    <select id="itDays">
                        <option value="3-5">3 - 5 Days</option>
                        <option value="6-9">6 - 9 Days</option>
                        <option value="10+">10+ Days</option>
                    </select>
                </div>
                <div>
                    <label>Your Email</label>
                    <input type="email" id="itEmail" required placeholder="name@domain.com">
                </div>
                <div>
                    <label>Special Requests / Vibe</label>
                    <textarea id="itNote" rows="2" placeholder="e.g. Adventure, honeymoon package, local food tour"></textarea>
                </div>
                <button type="submit" class="primary-btn" style="padding: 10px 20px; font-size: 13px; width: 100%; justify-content: center;">Generate Plan & Send Query</button>
            </form>
        `;
        addMessage('bot', formHtml, true);
        
        setTimeout(() => {
            const form = document.getElementById('itineraryForm');
            if (form) {
                form.onsubmit = function(e) {
                    e.preventDefault();
                    const dest = document.getElementById('itDest').value;
                    const days = document.getElementById('itDays').value;
                    const email = document.getElementById('itEmail').value;
                    const note = document.getElementById('itNote').value;
                    
                    form.innerHTML = '<p style="color:var(--accent-primary);margin:0;"><i class="fa fa-spinner fa-spin"></i> Submitting query...</p>';
                    
                    const formData = new FormData();
                    formData.append('email', email);
                    formData.append('destination', dest);
                    formData.append('duration', days);
                    formData.append('notes', note);
                    formData.append('type', 'Custom Itinerary Inquiry');
                    
                    fetch('https://formspree.io/f/xzzgaydr', {
                        method: 'POST',
                        body: formData,
                        headers: { 'Accept': 'application/json' }
                    }).then(() => {
                        form.innerHTML = '<span style="color:#10b981;font-weight:600;"><i class="fa fa-check"></i> Inquiry sent! We have emailed you your trip planner confirmation.</span>';
                        setTimeout(() => {
                            addMessage('bot', "Our local guide will reach out to you at " + email + " to finalize your trip schedule!");
                            addQuickReplies();
                        }, 2000);
                    }).catch(() => {
                        form.innerHTML = '<span style="color:#ef4444;"><i class="fa fa-times"></i> Submission error. Please try again.</span>';
                    });
                };
            }
        }, 100);
    }

    // Input message handler
    if (chatForm && chatInput) {
        chatForm.addEventListener('submit', function(e) {
            e.preventDefault();
            const text = chatInput.value.trim();
            if (!text) return;
            
            // Add user message
            addMessage('user', text);
            chatInput.value = '';
            
            // Bot replies
            botReply(text);
        });
    }

    // Welcome prompt triggers after 4 seconds
    setTimeout(() => {
        if (chatBody && chatBody.children.length === 0) {
            addMessage('bot', "Namaste! Welcome to Incredible India Travels. 🗺️ Let's design a custom travel package for you.");
            addQuickReplies();
            if (badge) badge.style.display = 'block'; // Show visual notification bubble
        }
    }, 4000);

    /* ==========================================================================
       5. DROPDOWN & CATEGORY FILTERS IN NAVIGATION BAR
       ========================================================================== */
    const navDropdownLinks = document.querySelectorAll('.dropdown-content li a');
    navDropdownLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            const filterClass = this.getAttribute('data-filter');
            if (filterClass && window.jQuery && jQuery.fn.isotope) {
                e.preventDefault();
                const $ = window.jQuery;
                
                // Update active filters list UI on middle portfolio
                $('.filters ul li').removeClass('active');
                $(`.filters ul li[data-filter="${filterClass}"]`).addClass('active');

                // Filter isotope
                $('.grid').isotope({ filter: filterClass });

                // Scroll to middle portfolio
                const portfolioSec = document.getElementById('middle');
                if (portfolioSec) {
                    portfolioSec.scrollIntoView({ behavior: 'smooth', block: 'start' });
                }
            }
        });
    });

});
