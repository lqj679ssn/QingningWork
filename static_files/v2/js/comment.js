$(document).ready(function () {
    var review_switcher = $('#review-switcher'),
        review_state = $('#review-state');
    review_switcher.on('change', function () {
        var checked = review_switcher.prop('checked');
        if (checked) {
            review_state.text('通过作品').removeClass('hint-danger').addClass('hint-success');
        }
        else {
            review_state.text('驳回作品（没有通过审核）').removeClass('hint-success').addClass('hint-danger');
        }
    });

    var comment_do = $('#comment-do'),
        comment_content = $('.comment-content');
    comment_do.on('click', function () {
        var post = {
            content: comment_content.val(),
            pass: (review_switcher === undefined) ? false : review_switcher.is(':checked'),
            event_id: comment_do.attr('data-event'),
            work_id: comment_do.attr('data-work'),
            owner_id: comment_do.attr('data-owner'),
        },
            json = encodedJSON(post);
        hide_comment_box();
        postJSON('/work/comment', json, function (response) {
            if (response.code !== 0) {
                show_hint(response.msg)
            }
            else {
                show_hint('评论成功');
                window.location.reload();
            }
        })
    });
});