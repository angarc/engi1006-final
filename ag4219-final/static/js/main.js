$('#subreddit-form-done-btn').click(function(e) {
  if($('#new-subreddit-input').val() == null) {
    return
  }

  postData = {
    subreddits: []
  }

  new_subreddit = $('#new-subreddit-input').val()

  $('.js-input').each(function(i, obj) {
    postData.subreddits.push($(this).val())
  });

  $('.subreddit-form').append("<div class='col-md-10'><div class='form-group'><input class='form-control js-input' value='"+ new_subreddit +"'/></div></div><div class='col-md-2'><i class='fa fa-trash'></i></div>")
  postData.subreddits.push(new_subreddit)
  $('#new-subreddit-input').val('')

  $.ajax({
    url: "/add-subreddit",
    method: 'POST',
    contentType: 'application/json; charset=utf-8',
    data: JSON.stringify(postData),
  })
})