var OwlCarousel = function () {
	return {
		initOwlCarousel: function () {
			$('.testimonials-v6').owlCarousel({
        loop: true,
        margin: 0,
        responsive: {
          0:{
            items: 1
          }
        },
        navText: [,],
        nav: true,
        dots: false,
			});

			$('.owl-clients-v5').owlCarousel({
        loop: true,
        margin: 0,
        responsive: {
					300:{
            items: 1
          },
          400:{
            items: 2
          },
          500:{
            items: 3
          },
          600:{
            items: 4
          },
          800:{
            items: 5
          },
          900:{
            items: 3
          },
          1000:{
            items: 3
          },
          1150:{
            items: 4
          },
          1300:{
            items: 5
          }
        },
        nav: false,
        dots: false,
			});
		}
	};
}();
