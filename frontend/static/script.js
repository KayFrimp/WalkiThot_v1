// Function to show/hide the sidebar
function showSidebar() {
    var sidebar = document.querySelector('.sidebar');
    sidebar.style.display = (sidebar.style.display === 'none' || sidebar.style.display === '') ? 'flex' : 'none';
}

// Function to toggle the mobile menu
function toggleMenu() {
    var nav = document.querySelector('header ul');
    nav.classList.toggle('show');
}

// Initialize the Slick carousel
$('.post-wrapper').slick({
    slidesToShow: 3,
    slidesToScroll: 1,
    autoplay: true,
    autoplaySpeed: 2000,
    nextArrow: $('.next'),
    prevArrow: $('.prev'), // Fixed the duplicated 'nextArrow' to 'prevArrow'
    responsive: [
        {
            breakpoint: 1024,
            settings: {
                slidesToShow: 3,
                slidesToScroll: 3,
                infinite: true,
                dots: true
            }
        },
        {
            breakpoint: 600,
            settings: {
                slidesToShow: 2,
                slidesToScroll: 2
            }
        },
        {
            breakpoint: 480,
            settings: {
                slidesToShow: 1,
                slidesToScroll: 1
            }
        }
    ]
});
