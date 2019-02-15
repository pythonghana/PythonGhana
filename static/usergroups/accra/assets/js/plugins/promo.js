$(function() {
  var PromoSlider = new MasterSlider();
  PromoSlider.setup('masterslider-promo' , {
	  width: 1400,    // PromoSlider standard width
	  height: 580,   // PromoSlider standard height
	  space: 1,
	  speed: 70,
	  layout: 'fullwidth',
	  loop: true,
	  preload: 0,
	  autoplay: true,
  });
  // adds Arrows navigation control to the PromoSlider.
  PromoSlider.control('arrows');
  PromoSlider.control('lightbox');
  PromoSlider.control('thumblist' , {autohide:false ,dir:'h',align:'bottom', width:200, height:120, margin:0, space:0 , hideUnder:500});
});
