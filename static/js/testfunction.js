function RT_music_name() {
    return '歌名';
}



$(function() {
    $("[data-toggle='popover']").popover({
        html : true,
        title: RT_music_name(),
        delay:{show:200, hide:500},
    });
});