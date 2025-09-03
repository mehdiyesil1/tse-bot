true == function() {
    //***********************//
    // telegram_bot function //
    //***********************//

    var TseHitSender = function(txtmessage) {
        const Http = new XMLHttpRequest();
        var url = 'https://tse-bot.mehdihassani3051.workers.dev/?text=' + encodeURIComponent(txtmessage);
        Http.open("GET", url);
        Http.send();
    };

    //************//
    let date = new Date();
    let nowDay = date.getDay();
    let nowHours = date.getHours();
    let nowMinute = date.getMinutes();
    var ntime = (new Date()).toLocaleString('fa-IR');

    //****************//
    function addCommas(a, c){
        if (typeof c == "undefined") { c = 2; }
        a += "";
        x = a.split(".");
        x1 = x[0];
        x2 = x.length > 1 ? (parseInt(x[1], 10) !== 0 ? "." + x[1].substring(0, c) : "") : "";
        var b = /(\d+)(\d{3})/;
        while (b.test(x1)) {
            x1 = x1.replace(b, "$1,$2");
        }
        return x1 + x2;
    }
    //*************//

    if([ih][0].PClosing != (pc) && [ih][0].ZTotTran != (tno) && [ih][0].QTotCap != (tval)){
        var len = [ih].length;
        if(typeof [ih][0].fixed == 'undefined'){
            for(var i=len;i>0;i--){
                if(typeof [ih][i] == 'undefined'){
                    [ih][i] = {};
                }
                [ih][i].PriceFirst = [ih][i-1].PriceFirst;
                [ih][i].PClosing = [ih][i-1].PClosing;
                [ih][i].PDrCotVal = [ih][i-1].PDrCotVal;
                [ih][i].ZTotTran = [ih][i-1].PriceFirst;
                [ih][i].QTotTran5J = [ih][i-1].QTotTran5J;
                [ih][i].QTotCap = [ih][i-1].QTotCap;
                [ih][i].PriceChange = [ih][i-1].PriceChange;
                [ih][i].PriceMin = [ih][i-1].PriceMin;
                [ih][i].PriceMax = [ih][i-1].PriceMax;
                [ih][i].PriceYesterday = [ih][i-1].PriceYesterday;
            }
            [ih][0].fixed = 1;
        }
        [ih][0].PriceFirst = (pf);
        [ih][0].PClosing = (pc);
        [ih][0].PDrCotVal = (pl);
        [ih][0].ZTotTran = (tno);
        [ih][0].QTotTran5J = (tvol);
        [ih][0].QTotCap = (tval);
        [ih][0].PriceChange = (pcc);
        [ih][0].PriceMin = (pmin);
        [ih][0].PriceMax = (pmax);
        [ih][0].PriceYesterday = (py);
    }

    // باقی کدها بدون تغییر، شامل RSI، Stochastic، حجم‌ها، فیلترها و ارسال به تلگرام
    // ... (کد کامل فیلترها و محاسبات دقیق را از نسخه قبلیت همین‌جا قرار بده)

    // مثال ارسال پیام اگر فیلترها برقرار باشند:
    if(x1==true || x2==true || x3==true || x4==true || x5==true || x6==true || x7==true || x8==true || x9==true){
        TseHitSender("پیام تست tse-bot");
    }

    return true;
}();
