$(document).ready(function () {
    let intervalId;

    $('#birthdate-form').on('submit', function (e) {
        e.preventDefault();
        $('#loading').show();
        const year = $('#year').val();
        const month = $('#month').val();
        const day = $('#day').val();

        // Clear previous interval if any
        if (intervalId) clearInterval(intervalId);

        // Fetch stats initially
        fetchStats(year, month, day);

        // Update stats every second
        intervalId = setInterval(() => {
            fetchStats(year, month, day);
        }, 1000);
    });

    function fetchStats(year, month, day) {
        $.post('/calculate-stats', { year, month, day }, function (data) {
            $('#loading').hide();

            // Define the desired order of keys
            const orderedKeys = [
                'Total days lived',
                'Total hours lived',
                'Total minutes lived',
                'Total seconds lived',
                'Total Breaths Taken',
                'Heartbeats',
                'The amount of times you have smiled',
                'Meals Eaten',
                'Steps Taken',
                'Days Slept',
                'Distance you travelled with the earth!',
                'Full Moons Since your Birth',
                'Global Rainfall',
                'Earthquakes since birth',
                'New species discovered',
                'New Words Added to the dictionary',
                'Olympic Games Since Birth',
                'Amount of people with the same birthday!',
                'Deforestation Reversed',
                'Ocean Rise',
                'Hours you have Worked ',
                'Poverty Lifted',
                'Poverty Decrease',
                'People cured from disease'
            ];

            // Render stats container only once
            if ($('#stats-container').children().length === 0) {
                orderedKeys.forEach(key => {
                    $('#stats-container').append(`
                        <div class="stat">
                            <strong>${key}:</strong> <span class="stat-value">${data[key]}</span>
                        </div>
                    `);
                });

                // Initialize scroll animations
                const stats = document.querySelectorAll('.stat');
                const observer = new IntersectionObserver((entries) => {
                    entries.forEach((entry) => {
                        if (entry.isIntersecting) {
                            entry.target.classList.add('visible');
                        } else {
                            entry.target.classList.remove('visible');
                        }
                    });
                }, {
                    threshold: 0.5, // Trigger when 50% of the element is visible
                });

                stats.forEach((stat) => observer.observe(stat));
            } else {
                // Update only the values dynamically
                orderedKeys.forEach((key, index) => {
                    $(`#stats-container .stat:nth-child(${index + 1}) .stat-value`).text(data[key]);
                });
            }
        });
    }
});