$(function() {
	var tpj=jQuery;
	var revapi104;
	tpj(document).ready(function() {
		if(tpj("#rev_slider_104_1").revolution == undefined){
			revslider_showDoubleJqueryError("#rev_slider_104_1");
		}else{
			revapi104 = tpj("#rev_slider_104_1").show().revolution({
				sliderType:"standard",
				jsFileLocation:"../../revolution/js/",
				sliderLayout:"fullscreen",
				dottedOverlay:"none",
				delay:9000,
				navigation: {
					keyboardNavigation:"off",
					keyboard_direction: "horizontal",
					mouseScrollNavigation:"off",
					onHoverStop:"off",
					touch:{
						touchenabled:"on",
						swipe_threshold: 75,
						swipe_min_touches: 1,
						swipe_direction: "horizontal",
						drag_block_vertical: false
					}
					,
					bullets: {
						enable:true,
						hide_onmobile:true,
						hide_under:960,
						style:"zeus",
						hide_onleave:false,
						direction:"horizontal",
						h_align:"right",
						v_align:"bottom",
						h_offset:80,
						v_offset:50,
						space:5,
						tmp:'<span class="tp-bullet-image"></span><span class="tp-bullet-imageoverlay"></span><span class="tp-bullet-title">{{title}}</span>'
					}
				},
				responsiveLevels:[1240,1024,778,480],
				gridwidth:[1240,1024,778,480],
				gridheight:[868,768,960,720],
				lazyType:"none",
				parallax: {
					type:"mouse",
					origo:"slidercenter",
					speed:2000,
					levels:[2,3,4,5,6,7,12,16,10,50],
					disable_onmobile:"on"
				},
				shadow:0,
				spinner:"off",
				stopLoop:"on",
				stopAfterLoops:0,
				stopAtSlide:1,
				shuffle:"off",
				autoHeight:"off",
				fullScreenAlignForce:"off",
				fullScreenOffsetContainer: "",
				fullScreenOffset: "60px",
				disableProgressBar:"on",
				hideThumbsOnMobile:"off",
				hideSliderAtLimit:0,
				hideCaptionAtLimit:0,
				hideAllCaptionAtLilmit:0,
				debugMode:false,
				fallbacks: {
					simplifyAll:"off",
					nextSlideOnWindowFocus:"off",
					disableFocusListener:false,
				}
			});
		var newCall = new Object(),
			cslide;

		newCall.callback = function() {
			var proc = revapi104.revgetparallaxproc(),
				fade = 1+proc,
				scale = 1+(Math.abs(proc)/10);

		    punchgs.TweenLite.set(revapi104.find('.slotholder, .rs-background-video-layer'),{opacity:fade,scale:scale});
		}
		newCall.inmodule = "parallax";
		newCall.atposition = "start";

		revapi104.bind("revolution.slide.onloaded",function (e) {
			revapi104.revaddcallback(newCall);
		});				}
	});	/*ready*/
});
