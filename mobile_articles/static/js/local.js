function load_articles(query_string) {
    var articles = "", title = "";
    for(var i = 0; i < localStorage.length; i++) {
        title = localStorage.key(i).trim();
        if (title.indexOf(query_string) > -1 && title !== 'last_update_date')
            articles += '<a onclick=\'display_article("' + title + '")\' href="#">' + title + '</a><br />';
    }
    return articles;
}

function display_article(title) {
    $('.content').html("");
    $('.title').html(title);
    $('.article').html(localStorage.getItem(title));
    return false;
}


$(function () {
    // article menus
    $('.content').html(load_articles(""));

    // single article
    title = $(".title").html();
    $('.article').html(localStorage.getItem(title));

    $('#main_form').submit(function () {
        $('.article, .title').html("");
        var last_update_date = localStorage.getItem("last_update_date");
        if (last_update_date == null) {
            // start from the beginning of time...
            last_update_date = (new Date(0)).toISOString();
        }
        $.ajax({
            url: "/articles/sync",
            data: "fetch_from=" + last_update_date,
            success: function (data) {
                console.log(data)
                var up_count = data.updated.length;
                for (var i = 0; i < up_count; i++) {
                    var article = data.updated[i];
                    localStorage.setItem(article[0], article[1]);
                    console.log("added: " + article)
                }
                var del_count = data.deleted.length;
                for (var i = 0; i < del_count; i++) {
                    var article = data.deleted[i];
                    localStorage.removeItem(article);
                    console.log("removed: " + article)
                }
                localStorage.setItem("last_update_date", (new Date()).toISOString());
                $('.content').html(load_articles(""));
            },
            error: function () {
                alert("error: no internet connection.");
            }
        });
        return false;
    })

    $('.search').click(function () {
        var val = $('#search').val()
        $('.article, .title').html("");
        $('.content').html(load_articles(val));
        return false;
    })
})