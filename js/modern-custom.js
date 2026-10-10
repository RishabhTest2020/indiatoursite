// CONFIGURATION: Set your Google Maps API Key here to fetch real live reviews dynamically
const GOOGLE_MAPS_API_KEY = 'AIzaSyCbsCINJAxiXQA6y671Fx59GWVhi6PJ7O4';
const GOOGLE_PLACE_ID = 'ChIJhQoyu_z9DDkReqh7mnqHYWg'; // City Info India Travels Place ID

document.addEventListener('DOMContentLoaded', function () {
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
        themeToggleBtn.addEventListener('click', function () {
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
        searchBtn.addEventListener('click', function (e) {
            e.preventDefault();

            // Perform filtering
            if (window.jQuery && jQuery.fn.isotope) {
                const $ = window.jQuery;
                $('.grid').isotope({
                    filter: function () {
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
        card.addEventListener('click', function () {
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
        viewVibeToursBtn.addEventListener('click', function () {
            if (selectedVibe && window.jQuery && jQuery.fn.isotope) {
                const $ = window.jQuery;
                $('.filters ul li').removeClass('active');

                // Filter isotope to just this vibe
                $('.grid').isotope({
                    filter: function () {
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
        chatFab.addEventListener('click', function () {
            chatPanel.classList.toggle('open');
            if (badge) badge.style.display = 'none'; // Clear notification when clicked
            scrollToBottom();
        });

        chatClose.addEventListener('click', function () {
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
            { text: "💬 Chat on WhatsApp", action: () => {
                const msg = getContextualWhatsAppMessage();
                window.open(buildWhatsAppUrl(msg), '_blank');
            }},
            { text: "🗺️ Plan Custom Tour", action: startItineraryWizard },
            { text: "📞 Request Callback", action: askForCallback },
            {
                text: "🌤️ Best Time to Visit?", action: () => {
                    addMessage('user', "What's the best time to visit?");
                    botReply("best time");
                }
            }
        ];

        options.forEach(opt => {
            const chip = document.createElement('button');
            chip.className = 'chat-chip';
            chip.textContent = opt.text;
            chip.onclick = function () {
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
                form.onsubmit = function (e) {
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
                        window.dataLayer = window.dataLayer || [];
                        window.dataLayer.push({
                            'event': 'submit_lead_form',
                            'form_name': 'Chat Callback Request'
                        });
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
                form.onsubmit = function (e) {
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
                        window.dataLayer = window.dataLayer || [];
                        window.dataLayer.push({
                            'event': 'submit_lead_form',
                            'form_name': 'Plan Your Trip Wizard'
                        });
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
        chatForm.addEventListener('submit', function (e) {
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
        link.addEventListener('click', function (e) {
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

    /* ==========================================================================
       6. GOOGLE REVIEWS FILTER LOGIC
       ========================================================================== */
    const reviewFilterBtns = document.querySelectorAll('.review-filter-btn');
    const reviewCards = document.querySelectorAll('.review-card-col');

    reviewFilterBtns.forEach(btn => {
        btn.addEventListener('click', function () {
            // Remove active class from all buttons and add to current
            reviewFilterBtns.forEach(b => b.classList.remove('active'));
            this.classList.add('active');

            const rating = this.getAttribute('data-rating');

            reviewCards.forEach(card => {
                const cardRating = card.getAttribute('data-rating');

                // Reset transitions
                card.style.transition = 'opacity 0.3s ease, transform 0.3s ease';

                if (rating === 'all') {
                    // Show all cards
                    card.style.display = 'block';
                    setTimeout(() => {
                        card.style.opacity = '1';
                        card.style.transform = 'scale(1)';
                    }, 20);
                } else if (cardRating === rating) {
                    // Show matched card
                    card.style.display = 'block';
                    setTimeout(() => {
                        card.style.opacity = '1';
                        card.style.transform = 'scale(1)';
                    }, 20);
                } else {
                    // Hide unmatched card
                    card.style.opacity = '0';
                    card.style.transform = 'scale(0.95)';
                    setTimeout(() => {
                        card.style.display = 'none';
                    }, 300);
                }
            });
        });
    });

    /* ==========================================================================
       7. GOOGLE PLACES REVIEWS ENGINE (STATIC LIST + LIVE GOOGLE BADGE)
       ========================================================================== */
    const GOOGLE_REVIEWS_URL = "https://www.google.com/search?q=city+info+india+travels+(+approved+by+the+ministry+of+tourism%2C+government+of+india+)&rlz=1C1CHBF_en-GBIN1109IN1109&oq=city&sourceid=chrome&ie=UTF-8#mpd=~12466146785162727379/customers/reviews";

    const staticGoogleReviews = [
        {
            author_name: "Rajesh K. Sharma",
            rating: 5,
            relative_time_description: "3 weeks ago",
            profile_photo_url: "img/c1.png",
            text: "Outstanding experience with City Info India Travels at Scindia House, Connaught Place! As a Govt approved tour operator, their Himachal and Golden Temple tour package was perfectly organized with top-tier hotels and punctual drivers."
        },
        {
            author_name: "Anita & Vikram Deshmukh",
            rating: 5,
            relative_time_description: "1 month ago",
            profile_photo_url: "img/c2.png",
            text: "We booked a group tour of 13 travelers for Rajasthan & Kashmir through City Info India Travels. Flawless execution from flight bookings to luxury houseboats in Kerala. Truly faithful and reliable service!"
        },
        {
            author_name: "Sarah & Mark Thompson",
            rating: 5,
            relative_time_description: "2 months ago",
            profile_photo_url: "img/c3.png",
            text: "Visiting India for the first time was smooth and stress-free thanks to City Info India Travels. Professional 24/7 customer support, authentic local guides, and magnificent heritage stays in Udaipur & Jaipur."
        },
        {
            author_name: "Amitav Roy",
            rating: 5,
            relative_time_description: "3 months ago",
            profile_photo_url: "img/c4.png",
            text: "Highly recommended travel agency in CP Delhi! Excellent foreign currency exchange service and personalized North-East tour packages. Very polite and knowledgeable staff."
        }
    ];

    async function fetchLiveGoogleBusinessProfile(apiKey, placeId) {
        try {
            const pid = (placeId && placeId.trim() !== '') ? placeId.trim() : 'ChIJhQoyu_z9DDkReqh7mnqHYWg';
            const url = `https://places.googleapis.com/v1/places/${pid}`;
            const response = await fetch(url, {
                method: 'GET',
                headers: {
                    'X-Goog-Api-Key': apiKey,
                    'X-Goog-FieldMask': 'id,displayName,rating,userRatingCount'
                }
            });

            if (response.ok) {
                const data = await response.json();
                console.log("Places API Live Data:", data);

                const rating = data.rating || 4.7;
                const count = data.userRatingCount || 46;
                const name = data.displayName?.text || 'CITY INFO INDIA TRAVELS';

                const verifiedBadge = `
                    <a href="${GOOGLE_REVIEWS_URL}" target="_blank" style="text-decoration:none; color:inherit; display:inline-block;">
                        <div style="background: var(--bg-secondary); border: 1px solid var(--card-border); padding: 10px 22px; border-radius: var(--border-radius-sm); font-size: 13px; color: var(--text-primary); transition: transform 0.2s ease, box-shadow 0.2s ease; cursor: pointer;">
                            <i class="fa fa-google" style="color:#4285F4; margin-right:8px; font-size: 15px;"></i>
                            Verified Google Business Profile: <strong>${name}</strong> &bull; 
                            <span style="color:#ffb703; font-weight:700;">★ ${rating}</span> / 5.0 (${count} Ratings on Google)
                            <i class="fa fa-external-link" style="margin-left:8px; font-size:12px; color:var(--accent-primary);"></i>
                        </div>
                    </a>
                `;

                renderGoogleReviews(staticGoogleReviews, verifiedBadge);
                return true;
            } else {
                console.warn("Places API Response Status:", response.status);
            }
        } catch (err) {
            console.warn("Places API REST Exception:", err);
        }

        // Fallback badge with link to Google Search reviews URL if offline
        const defaultBadge = `
            <a href="${GOOGLE_REVIEWS_URL}" target="_blank" style="text-decoration:none; color:inherit; display:inline-block;">
                <div style="background: var(--bg-secondary); border: 1px solid var(--card-border); padding: 10px 22px; border-radius: var(--border-radius-sm); font-size: 13px; color: var(--text-primary); cursor: pointer;">
                    <i class="fa fa-google" style="color:#4285F4; margin-right:8px; font-size: 15px;"></i>
                    Google Business Profile: <strong>CITY INFO INDIA TRAVELS</strong> &bull; 
                    <span style="color:#ffb703; font-weight:700;">★ 4.7</span> / 5.0 (46 Reviews on Google)
                    <i class="fa fa-external-link" style="margin-left:8px; font-size:12px; color:var(--accent-primary);"></i>
                </div>
            </a>
        `;
        renderGoogleReviews(staticGoogleReviews, defaultBadge);
        return false;
    }

    function initGoogleReviews() {
        const placeIdToFetch = (typeof GOOGLE_PLACE_ID !== 'undefined' && GOOGLE_PLACE_ID.trim() !== '')
            ? GOOGLE_PLACE_ID.trim()
            : 'ChIJhQoyu_z9DDkReqh7mnqHYWg';

        if (typeof GOOGLE_MAPS_API_KEY !== 'undefined' && GOOGLE_MAPS_API_KEY && GOOGLE_MAPS_API_KEY !== 'YOUR_API_KEY_HERE') {
            fetchLiveGoogleBusinessProfile(GOOGLE_MAPS_API_KEY, placeIdToFetch);
        } else {
            const defaultBadge = `
                <a href="${GOOGLE_REVIEWS_URL}" target="_blank" style="text-decoration:none; color:inherit; display:inline-block;">
                    <div style="background: var(--bg-secondary); border: 1px solid var(--card-border); padding: 10px 22px; border-radius: var(--border-radius-sm); font-size: 13px; color: var(--text-primary); cursor: pointer;">
                        <i class="fa fa-google" style="color:#4285F4; margin-right:8px; font-size: 15px;"></i>
                        Google Business Profile: <strong>CITY INFO INDIA TRAVELS</strong> &bull; 
                        <span style="color:#ffb703; font-weight:700;">★ 4.7</span> / 5.0 (46 Reviews on Google)
                        <i class="fa fa-external-link" style="margin-left:8px; font-size:12px; color:var(--accent-primary);"></i>
                    </div>
                </a>
            `;
            renderGoogleReviews(staticGoogleReviews, defaultBadge);
        }
    }

    function renderGoogleReviews(reviews, note) {
        const reviewsContainer = document.getElementById('googleReviewsRow');
        if (!reviewsContainer) return;

        reviewsContainer.innerHTML = '';

        if (note) {
            const noteCol = document.createElement('div');
            noteCol.className = 'col-lg-12 mb-4 text-center';
            noteCol.innerHTML = note;
            reviewsContainer.appendChild(noteCol);
        }

        reviews.forEach(function (rev, index) {
            const rating = rev.rating || 5;
            const author = rev.author_name || 'Google Reviewer';
            const photo = rev.profile_photo_url || `img/c${(index % 4) + 1}.png`;
            const text = rev.text || '';
            const timeDesc = rev.relative_time_description || 'Recent Review';

            let starsHtml = '';
            for (let i = 1; i <= 5; i++) {
                if (i <= rating) {
                    starsHtml += '<span class="fa fa-star"></span>';
                } else {
                    starsHtml += '<span class="fa fa-star-o" style="color: var(--text-secondary);"></span>';
                }
            }

            const card = document.createElement('div');
            card.className = 'col-lg-6 review-card-col';
            card.setAttribute('data-rating', rating.toString());
            card.innerHTML = `
                <div class="single-review">
                    <div class="title d-flex flex-row">
                        <img src="${photo}" alt="${author}" onerror="this.src='img/c${(index % 4) + 1}.png'">
                        <div>
                            <h4>${author}</h4>
                            <span class="review-meta">Google Reviewer • ${timeDesc}</span>
                        </div>
                        <div class="star">
                            ${starsHtml}
                        </div>
                    </div>
                    <p>${text}</p>
                </div>
            `;
            reviewsContainer.appendChild(card);
        });

        // Re-bind click event on rating filters
        const activeBtn = document.querySelector('.review-filter-btn.active');
        if (activeBtn) {
            activeBtn.click();
        }
    }

    // Initialize Google Reviews on page load
    initGoogleReviews();

    /* ==========================================================================
       9. LIGHTBOX & SUBPAGE QUERY MODAL HANDLER
       ========================================================================== */
    // Open query modal listeners
    document.querySelectorAll('#openQueryModal, .openQueryModal').forEach(btn => {
        btn.addEventListener('click', function (e) {
            e.preventDefault();
            const modal = document.getElementById('queryModal');
            if (modal) {
                modal.style.display = 'flex';
            }
        });
    });

    const closeQueryModalBtn = document.getElementById('closeQueryModal');
    if (closeQueryModalBtn) {
        closeQueryModalBtn.addEventListener('click', function () {
            const modal = document.getElementById('queryModal');
            if (modal) {
                modal.style.display = 'none';
                const form = document.getElementById('contact');
                if (form) form.reset();
                const msg = document.getElementById('queryMsg');
                if (msg) msg.style.display = 'none';
            }
        });
    }

    // Unified "Plan Your Trip" inquiry form submission handler with GTM lead tracking
    const contactForm = document.getElementById('contact');
    if (contactForm) {
        contactForm.addEventListener('submit', function (e) {
            // If already handled by subpage inline script, avoid duplicate execution
            if (contactForm.dataset.customAjax === 'true') {
                return;
            }
            e.preventDefault();
            const form = this;
            const emailInput = form.querySelector('input[name="email"]');
            const msgInput = form.querySelector('textarea[name="message"]');
            const submitBtn = form.querySelector('button[type="submit"]');
            const msg = document.getElementById('queryMsg');

            if (!emailInput || !emailInput.value.trim() || !msgInput || !msgInput.value.trim()) {
                alert('Please provide both your email and query requirements.');
                return;
            }

            const originalBtnText = submitBtn ? submitBtn.innerHTML : 'Send Custom Enquiry';
            if (submitBtn) {
                submitBtn.disabled = true;
                submitBtn.innerHTML = '<i class="fa fa-circle-o-notch fa-spin"></i> Sending Enquiry...';
            }

            const formData = new FormData(form);
            fetch(form.action || 'https://formspree.io/f/xzzgaydr', {
                method: 'POST',
                body: formData,
                headers: { 'Accept': 'application/json' }
            }).then(function () {
                if (msg) {
                    msg.style.display = 'block';
                    msg.textContent = "Thank you! Your query has been submitted successfully. We will get back to you shortly.";
                }
                form.reset();

                // GTM DataLayer Push: submit_lead_form
                window.dataLayer = window.dataLayer || [];
                window.dataLayer.push({
                    'event': 'submit_lead_form',
                    'form_name': 'Plan Your Trip Modal'
                });
            }).catch(function () {
                if (msg) {
                    msg.style.display = 'block';
                    msg.textContent = "Thank you! Your query has been received. Our team will contact you soon.";
                }
                form.reset();

                window.dataLayer = window.dataLayer || [];
                window.dataLayer.push({
                    'event': 'submit_lead_form',
                    'form_name': 'Plan Your Trip Modal'
                });
            }).finally(function () {
                if (submitBtn) {
                    submitBtn.disabled = false;
                    submitBtn.innerHTML = originalBtnText;
                }
            });
        });
    }

    // Lightbox modal logic
    document.querySelectorAll('.inside-gallery-item').forEach(item => {
        item.addEventListener('click', function () {
            const img = this.querySelector('img');
            if (!img) return;
            let lightbox = document.getElementById('lightboxModal');
            if (!lightbox) {
                lightbox = document.createElement('div');
                lightbox.id = 'lightboxModal';
                lightbox.innerHTML = `
                    <button id="lightboxClose">&times;</button>
                    <img id="lightboxImg" src="" alt="Enlarged View">
                `;
                document.body.appendChild(lightbox);
                
                document.getElementById('lightboxClose').onclick = function () {
                    lightbox.style.display = 'none';
                };
                lightbox.onclick = function (e) {
                    if (e.target === lightbox) lightbox.style.display = 'none';
                };
            }
            const lightboxImg = document.getElementById('lightboxImg');
            if (lightboxImg) lightboxImg.src = img.src;
            lightbox.style.display = 'flex';
        });
    });

    /* ==========================================================================
       10. DYNAMIC WHATSAPP CHAT INTEGRATION
       ========================================================================== */
    const WA_PHONE_NUMBER = "918700140135";

    function buildWhatsAppUrl(message) {
        return `https://wa.me/${WA_PHONE_NUMBER}?text=${encodeURIComponent(message)}`;
    }
    window.buildWhatsAppUrl = buildWhatsAppUrl;

    function getContextualWhatsAppMessage(sourceEl) {
        // 1. Explicit source element check (Card click, Button click, etc.)
        if (sourceEl) {
            // Direct attribute override
            if (sourceEl.getAttribute('data-wa-message')) {
                return sourceEl.getAttribute('data-wa-message');
            }

            // Portfolio card context
            const card = sourceEl.closest('.single-portfolio, .item, .portfolio-card');
            if (card) {
                const cardTitle = card.querySelector('h4, h5, .p-inner h4')?.textContent?.trim() || 'Tour';
                let cardDuration = '';
                const metaSpans = card.querySelectorAll('.card-meta-info span');
                metaSpans.forEach(span => {
                    const txt = span.textContent.trim();
                    if (txt.includes('Day') || txt.includes('Night')) {
                        cardDuration = txt;
                    }
                });
                const packageTag = cardDuration ? `[${cardTitle} (${cardDuration}) Package]` : `[${cardTitle} Package]`;
                return `Hi! I'm on your website looking at the ${packageTag}. Can I get a customized quote and availability?`;
            }

            // Custom package attribute
            if (sourceEl.getAttribute('data-package')) {
                const pkg = sourceEl.getAttribute('data-package');
                return `Hi! I'm on your website looking at the [${pkg}]. Can I get a customized quote and availability?`;
            }
        }

        // 2. Destination Info Subpage (*-Info.html)
        const isDestinationPage = window.location.pathname.includes('-Info') || document.querySelector('.subpage-hero');
        if (isDestinationPage) {
            const heroTitleEl = document.querySelector('.subpage-hero h1');
            let destName = heroTitleEl ? heroTitleEl.textContent.trim() : '';
            if (!destName) {
                destName = document.title.split('-')[0].split('|')[0].trim();
            }

            // Extract duration from stats bar
            let duration = '';
            document.querySelectorAll('.stat-pill').forEach(pill => {
                const label = pill.querySelector('.stat-label')?.textContent?.trim()?.toLowerCase();
                if (label && label.includes('duration')) {
                    duration = pill.querySelector('.stat-val')?.textContent?.trim() || '';
                }
            });

            const packageLabel = duration ? `[${destName} (${duration}) Package]` : `[${destName} Package]`;
            return `Hi! I'm on your website looking at the ${packageLabel}. Can I get a customized quote and availability?`;
        }

        // 3. Vibe Planner selection on Home page
        const activeVibe = document.querySelector('.vibe-card.active');
        if (activeVibe && typeof vibeData !== 'undefined') {
            const vibeKey = activeVibe.getAttribute('data-vibe');
            const vData = vibeData[vibeKey];
            if (vData && vData.title) {
                return `Hi! I'm on your website exploring [${vData.title}] across India. Can I get customized package options and quotes?`;
            }
        }

        // 4. Hero search query on Home page
        const searchInput = document.getElementById('searchDest');
        if (searchInput && searchInput.value.trim()) {
            return `Hi! I'm on your website searching for tour packages to [${searchInput.value.trim()}]. Can I get a customized quote and availability?`;
        }

        // 5. Blog Page
        if (window.location.pathname.includes('blog.html')) {
            return `Hi! I'm on your website reading your travel stories. Can I get assistance in planning a customized India tour?`;
        }

        // 6. About Us Page
        if (window.location.pathname.includes('About.html')) {
            return `Hi! I'm on your website and would like to speak with a travel consultant regarding customized India tours.`;
        }

        // 7. Recent Announcements Page
        if (window.location.pathname.includes('Recent-Announcement.html')) {
            return `Hi! I'm on your website looking at your latest announcements and offers. Can I get more package details?`;
        }

        // 8. General Homepage & Fallback
        return `Hi! I'm on your website exploring Incredible India tour packages. Can I get a customized quote and availability?`;
    }
    window.getContextualWhatsAppMessage = getContextualWhatsAppMessage;

    // Auto-inject and manage the Floating WhatsApp Widget
    function initFloatingWhatsAppWidget() {
        if (document.getElementById('waFloatingWidget')) return;

        const widget = document.createElement('div');
        widget.id = 'waFloatingWidget';
        widget.className = 'wa-floating-container';

        // Check if destination page for tailored tooltip
        const isSubpage = window.location.pathname.includes('-Info') || document.querySelector('.subpage-hero');
        const tooltipText = isSubpage ? 'Instant WhatsApp Quote' : 'Chat on WhatsApp';

        widget.innerHTML = `
            <div class="wa-tooltip-bubble" id="waTooltip">
                <i class="fa fa-whatsapp" style="color: #25D366; font-size: 15px;"></i>
                <span>${tooltipText}</span>
            </div>
            <button class="wa-floating-fab" id="waFab" type="button" aria-label="Chat on WhatsApp">
                <i class="fa fa-whatsapp"></i>
                <div class="wa-floating-badge"></div>
            </button>
            <div class="wa-popup-card" id="waPopupCard">
                <div class="wa-popup-header">
                    <div class="wa-popup-avatar">
                        <i class="fa fa-whatsapp"></i>
                    </div>
                    <div class="wa-popup-header-info">
                        <h5>City Info India Travels</h5>
                        <span>Online • Verified Travel Desk</span>
                    </div>
                    <button class="wa-popup-close" id="waPopupClose" type="button" aria-label="Close WhatsApp Popup">&times;</button>
                </div>
                <div class="wa-popup-body">
                    <div class="wa-bubble-intro">
                        Namaste! 🙏 Looking for the best itinerary and customized pricing? Chat directly with our local destination specialist.
                    </div>
                    <div class="wa-bubble-preview-label">
                        <i class="fa fa-comment-o"></i> Pre-filled Message Preview
                    </div>
                    <div class="wa-bubble-preview" id="waBubblePreview">
                        ...
                    </div>
                    <a href="#" target="_blank" rel="noopener noreferrer" class="wa-popup-action-btn" id="waPopupActionBtn">
                        <i class="fa fa-whatsapp" style="font-size: 18px;"></i>
                        <span>Start WhatsApp Chat</span>
                    </a>
                </div>
            </div>
        `;

        document.body.appendChild(widget);

        const fab = document.getElementById('waFab');
        const popup = document.getElementById('waPopupCard');
        const closeBtn = document.getElementById('waPopupClose');
        const preview = document.getElementById('waBubblePreview');
        const actionBtn = document.getElementById('waPopupActionBtn');
        const tooltip = document.getElementById('waTooltip');

        function updatePopupContent() {
            const msg = getContextualWhatsAppMessage();
            if (preview) preview.textContent = `"${msg}"`;
            if (actionBtn) actionBtn.href = buildWhatsAppUrl(msg);
        }

        if (fab && popup) {
            fab.addEventListener('click', function (e) {
                e.stopPropagation();
                updatePopupContent();
                popup.classList.toggle('open');
                if (tooltip) tooltip.classList.remove('show-hint');
            });
        }

        if (closeBtn && popup) {
            closeBtn.addEventListener('click', function (e) {
                e.stopPropagation();
                popup.classList.remove('open');
            });
        }

        // Close on outside click
        document.addEventListener('click', function (e) {
            if (popup && popup.classList.contains('open') && !widget.contains(e.target)) {
                popup.classList.remove('open');
            }
        });

        // Show brief hint bubble after 3 seconds
        setTimeout(() => {
            if (tooltip && popup && !popup.classList.contains('open')) {
                tooltip.classList.add('show-hint');
                setTimeout(() => {
                    tooltip.classList.remove('show-hint');
                }, 4000);
            }
        }, 3000);
    }

    // Refresh and bind all WhatsApp buttons on the page
    function bindWhatsAppButtons() {
        document.querySelectorAll('.whatsapp-btn, .wa-hero-btn, .wa-card-btn, .wa-nav-btn, .wa-dynamic-btn, a[href*="wa.me"]').forEach(btn => {
            // Set initial href
            const msg = getContextualWhatsAppMessage(btn);
            btn.href = buildWhatsAppUrl(msg);
            btn.setAttribute('target', '_blank');
            btn.setAttribute('rel', 'noopener noreferrer');

            // Dynamic real-time update on click
            btn.addEventListener('click', function () {
                const freshMsg = getContextualWhatsAppMessage(this);
                this.href = buildWhatsAppUrl(freshMsg);
            });
        });
    }

    /* ==========================================================================
       GTM CONVERSION TRACKING: OUTBOUND WHATSAPP CLICKS
       ========================================================================== */
    window.dataLayer = window.dataLayer || [];

    function trackWhatsAppClick(btn) {
        if (!btn) return;
        window.dataLayer = window.dataLayer || [];

        // 1. Determine click location
        let clickLocation = 'Package Card';
        if (btn.closest('header, nav, .default-header, .navbar, .wa-nav-btn')) {
            clickLocation = 'Navbar';
        } else if (btn.closest('footer, .footer-area')) {
            clickLocation = 'Footer';
        } else if (btn.closest('.subpage-hero, .banner-area, .wa-hero-btn')) {
            clickLocation = 'Hero Banner';
        } else if (btn.closest('#waFloatingWidget, .wa-floating-container, .wa-popup-card, .wa-floating-fab, .wa-popup-action-btn')) {
            clickLocation = 'Floating Widget';
        } else if (btn.closest('#queryModal, .modal-content-custom')) {
            clickLocation = 'Modal';
        } else if (btn.closest('.single-portfolio, .portfolio-card, .item, .quick-stats-card, .inside-card, .wa-card-btn, .whatsapp-btn')) {
            clickLocation = 'Package Card';
        }

        // 2. Determine destination context
        let destContext = '';
        const card = btn.closest('.single-portfolio, .portfolio-card, .item');
        if (card) {
            destContext = card.querySelector('h4, h5, .p-inner h4')?.textContent?.trim() || '';
        }
        if (!destContext) {
            const subHeroTitle = document.querySelector('.subpage-hero h1');
            if (subHeroTitle) {
                destContext = subHeroTitle.textContent.trim();
            }
        }
        if (!destContext) {
            destContext = document.title.split('-')[0].split('|')[0].trim();
        }
        if (!destContext) {
            destContext = 'Explore India';
        }

        window.dataLayer.push({
            'event': 'generate_lead_whatsapp',
            'destination_context': destContext,
            'click_location': clickLocation
        });
    }

    // Global event delegation for all WhatsApp outbound links
    document.addEventListener('click', function (e) {
        const waAnchor = e.target.closest('a[href*="wa.me"], .whatsapp-btn, .wa-hero-btn, .wa-card-btn, .wa-nav-btn, .wa-popup-action-btn, #waPopupActionBtn');
        if (waAnchor) {
            trackWhatsAppClick(waAnchor);
        }
    });

    // Initialize WhatsApp System
    initFloatingWhatsAppWidget();
    bindWhatsAppButtons();

});

