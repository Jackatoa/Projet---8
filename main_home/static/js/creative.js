(function ($) {
    "use strict"; // Start of use strict

    // Smooth scrolling using jQuery easing
    $('a.js-scroll-trigger[href*="#"]:not([href="#"])').click(function () {
        if (location.pathname.replace(/^\//, '') == this.pathname.replace(/^\//, '') && location.hostname == this.hostname) {
            var target = $(this.hash);
            target = target.length ? target : $('[name=' + this.hash.slice(1) + ']');
            if (target.length) {
                $('html, body').animate({
                    scrollTop: (target.offset().top - 72)
                }, 1000, "easeInOutExpo");
                return false;
            }
        }
    });

    // Closes responsive menu when a scroll trigger link is clicked
    $('.js-scroll-trigger').click(function () {
        $('.navbar-collapse').collapse('hide');
    });

    // Activate scrollspy to add active class to navbar items on scroll
    $('body').scrollspy({
        target: '#mainNav',
        offset: 75
    });

    // Collapse Navbar
    var navbarCollapse = function () {
        if ($("#mainNav").offset().top > 100) {
            $("#mainNav").addClass("navbar-scrolled");
        } else {
            $("#mainNav").removeClass("navbar-scrolled");
        }
    };
    // Collapse now if page is not at top
    navbarCollapse();
    // Collapse the navbar when page is scrolled
    $(window).scroll(navbarCollapse);

    // Magnific popup calls
    $('#portfolio').magnificPopup({
        delegate: 'a',
        type: 'image',
        tLoading: 'Loading image #%curr%...',
        mainClass: 'mfp-img-mobile',
        gallery: {
            enabled: true,
            navigateByImgClick: true,
            preload: [0, 1]
        },
        image: {
            tError: '<a href="%url%">The image #%curr%</a> could not be loaded.'
        }
    });

})(jQuery); // End of use strict
Vue.config.devtools = true;


function BrowserDetection() {
    //Check if browser is IE
    if (navigator.userAgent.search("Firefox") & gt;
    = 0
)
    {
        Vue.component('card', {
            template: `
    <div class="card-wrap"
      @mousemove="handleMouseMove"
      @mouseenter="handleMouseEnter"
      @mouseleave="handleMouseLeave"
      ref="card">
      <div class="card"
        :style="cardStyle">
        <div class="card-bg" :style="[cardBgTransform, cardBgImage]"></div>
         <slot name="nutri"></slot>
        <div class="card-info">
          <slot name="header"></slot>
          <slot name="content"></slot>
          <slot name="save"></slot>
        </div>
      </div>
    </div>`,
            mounted() {
                this.width = this.$refs.card.offsetWidth;
                this.height = this.$refs.card.offsetHeight;
            },
            props: ['dataImage'],
            data: () => ({
                width: 0,
                height: 0,
                mouseX: 0,
                mouseY: 0,
                mouseLeaveDelay: null
            }),

            computed: {
                mousePX() {
                    return this.mouseX / this.width;
                },
                mousePY() {
                    return this.mouseY / this.height;
                },
                cardStyle() {
                    const rX = this.mousePX * 30;
                    const rY = this.mousePY * -30;
                    return {
                        transform: `rotateY(${rX}deg) rotateX(${rY}deg)`
                    };

                },
                cardBgTransform() {
                    const tX = this.mousePX * -40;
                    const tY = this.mousePY * -40;
                    return {
                        transform: `translateX(${tX}px) translateY(${tY}px)`
                    };

                },
                cardBgImage() {
                    return {
                        backgroundImage: `url(${this.dataImage})`
                    };

                }
            },

            methods: {
                handleMouseMove(e) {
                    this.mouseX = e.pageX - this.$refs.card.offsetLeft - this.width / 2;
                    this.mouseY = e.pageY - this.$refs.card.offsetTop - this.height / 2;
                },
                handleMouseEnter() {
                    clearTimeout(this.mouseLeaveDelay);
                },
                handleMouseLeave() {
                    this.mouseLeaveDelay = setTimeout(() => {
                        this.mouseX = 0;
                        this.mouseY = 0;
                    }, 1000);
                }
            }
        });


        const app = new Vue({
            el: '#app'
        });
        // insert conditional IE code here
    }
    //Check if browser is Chrome
else
    {
        // insert conditional Chrome code hereVue.component('card', {
        //     template: `
        //     <div class="card-wrap"
        //       @mousemove="handleMouseMove"
        //       @mouseenter="handleMouseEnter"
        //       @mouseleave="handleMouseLeave"
        //       ref="card">
        //       <div class="card"
        //         :style="cardStyle">
        //         <div class="card-bg" :style="[cardBgTransform, cardBgImage]"></div>
        //          <slot name="nutri"></slot>
        //         <div class="card-info">
        //           <slot name="header"></slot>
        //           <slot name="content"></slot>
        //           <slot name="save"></slot>
        //         </div>
        //       </div>
        //     </div>`,
        //     mounted() {
        //         this.width = this.$refs.card.offsetWidth;
        //         this.height = this.$refs.card.offsetHeight;
        //     },
        //     props: ['dataImage'],
        //     data: () => ({
        //         width: 0,
        //         height: 0,
        //         mouseX: 0,
        //         mouseY: 0,
        //         mouseLeaveDelay: null
        //     }),
        //
        //     computed: {
        //         mousePX() {
        //             return this.mouseX / this.width;
        //         },
        //         mousePY() {
        //             return this.mouseY / this.height;
        //         },
        //         cardStyle() {
        //             const rX = this.mousePX * 30;
        //             const rY = this.mousePY * -30;
        //             return {
        //                 transform: `rotateY(${rX}deg) rotateX(${rY}deg)`
        //             };
        //
        //         },
        //         cardBgTransform() {
        //             const tX = this.mousePX * -40;
        //             const tY = this.mousePY * -40;
        //             return {
        //                 transform: `translateX(${tX}px) translateY(${tY}px)`
        //             };
        //
        //         },
        //         cardBgImage() {
        //             return {
        //                 backgroundImage: `url(${this.dataImage})`
        //             };
        //
        //         }
        //     },
        //
        //     methods: {
        //         handleMouseMove(e) {
        //             this.mouseX = e.pageX - this.$refs.card.offsetLeft - this.width / 2;
        //             this.mouseY = e.pageY - this.$refs.card.offsetTop - this.height / 2;
        //         },
        //         handleMouseEnter() {
        //             clearTimeout(this.mouseLeaveDelay);
        //         },
        //         handleMouseLeave() {
        //             this.mouseLeaveDelay = setTimeout(() => {
        //                 this.mouseX = 0;
        //                 this.mouseY = 0;
        //             }, 1000);
        //         }
        //     }
        // });
        //
        //
        // const app = new Vue({
        //     el: '#app'
        // });
    }
}


var modal = document.getElementById("myModal");

// Get the image and insert it inside the modal - use its "alt" text as a caption
var img = document.getElementById("myImg");
var img2 = document.getElementById("myImg2");
var modalImg = document.getElementById("img01");
var captionText = document.getElementById("caption");
img.onclick = function () {
    modal.style.display = "block";
    modalImg.src = this.src;
    captionText.innerHTML = this.alt;
}
img2.onclick = function () {
    modal.style.display = "block";
    modalImg.src = this.src;
    captionText.innerHTML = this.alt;
}
// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

// When the user clicks on <span> (x), close the modal
span.onclick = function () {
    modal.style.display = "none";
}

function visibleform() {
    var x = document.getElementById("updateform");
    if (x.style.display === "block") {
        x.style.display = "none";
    } else {
        x.style.display = "block";
    }
}

$(document).ready(function () {
    $('[data-toggle="tooltip"]').tooltip();
});

