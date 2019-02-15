var OwlCarousel = function () {
	return {
		initOwlCarousel: function () {
			$('.our-services-list').owlCarousel( {
				loop: true,
				margin: 0,
        responsive: {
          0:{
            items: 1
          },
          500:{
            items: 2
          },
          700:{
            items: 3
          }
        },
				navText: [,],
				nav: true,
				dots: false,
				navContainerClass: 'owl-buttons',
			});
			$('.our-tours-list').owlCarousel( {
				loop: true,
				margin: 15,
        responsive: {
          0:{
            items: 1
          },
          500: {
          	items: 2
          },
          650: {
          	items: 3
          },
          850:{
            items: 4
          },
          1024:{
            items: 5
          },
          1270:{
            items: 6
          }
        },
				navText: [,],
				nav: true,
				dots: false,
				navContainerClass: 'owl-buttons',
			});
		}
	};
}();
