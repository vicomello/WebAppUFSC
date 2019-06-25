/* #TODO */
            var top = ($('.scrollTop').offset() || { "top": NaN }).top;
            if (isNaN(top)) {
                alert("something is wrong, no top");
            } else {
                $('html, body').stop().animate({
                'scrollTop': $target.offset().top
            }, cfg.scrollDuration, 'swing').promise().done(function () {

                // check if menu is open
                if ($('body').hasClass('menu-is-open')) {
                    $('.header-menu-toggle').trigger('click');
                }

                window.location.hash = target;
            });
            }