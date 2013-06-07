function load_articles(query_string) {
    var articles = "", title = "";
    for(var i = 0; i < localStorage.length; i++) {
        title = localStorage.key(i)
        if (title.indexOf(query_string) > -1)
            articles += '<a href="/articles/?title=' + encodeURI(title) + '">' + title + '</a><br />';
    }
    return articles;
}


$(function () {
    // article menus
    $('.content').html(load_articles(""));

    // single article
    title = $(".title").html();
    $('.article').html(localStorage.getItem(title));

    $('#main_form').submit(function () {
        $('.content').load(
            "/articles/sync"
        );
        return false;
    })

    $('.search').click(function () {
        var val = $('#search').val()
        $('.article, .title').hide();
        $('.content').removeClass('hidden');
        $('.content').html(load_articles(val));
        return false;
    })
})