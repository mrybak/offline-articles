function load_articles(query_string) {
    var articles = "", title = "";
    for(var i = 0; i < localStorage.length; i++) {
        title = localStorage.key(i).trim();
        if (title.indexOf(query_string) > -1)
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
        $('.content').load(
            "/articles/sync",
            function (responseText, textStatus, req) {
                if (textStatus == "error")
                    alert("error: no internet connection.");
            }
        );
        return false;
    })

    $('.search').click(function () {
        var val = $('#search').val()
        $('.article, .title').html("");
        $('.content').html(load_articles(val));
        return false;
    })
})