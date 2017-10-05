    //OUR SERVICES
    $('.service').click(function () {
        var $t = $(this);
        if (tabFinish || $t.hasClass('active')) return false;
        tabFinish = 1;
        $t.closest('.serv').find('.service').removeClass('active-item');
        $t.addClass('active-item');
        var index = $t.parent().find('.service').index(this);
        $t.closest('.serv').find('.serv-description:visible').fadeOut(500, function () {
            $t.closest('.serv').find('.serv-description').eq(index).fadeIn(500,
                function () {
                    tabFinish = 0;

                });
        });
    });

    var tabFinish = 0;

    $('.about-2-icon-box').click(function () {
        var $t = $(this);
        if (tabFinish || $t.hasClass('active')) return false;
        tabFinish = 1;
        $t.closest('.about-2').find('.about-2-icon-box').removeClass('active-item');
        $t.addClass('.active-item');
        var index = $t.parent().find('.about-icon-2-box').index(this);
        $t.closest('.about-2').find('.about-description:visible').fadeOut(500, function () {
            $t.closest('.about-2').find('.about-description').eq(index).fadeIn(500,
            function () {
                tabFinish = 0;
            })
        })
    });