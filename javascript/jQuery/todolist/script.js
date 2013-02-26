$(document).ready(function() {

    $('.list-box').append('<div class="no-item"><p>There is not items in your list<p/></div>');


    $('input[name=itemToAdd]').keypress(function(e){
        if(e.which == 13){
            return false;
        }
    });


    var count = 0;
    console.log(count);
    $('#button').click(function(){
        var input = $('input[name=itemToAdd]');
        var toAdd = input.val();
        if(count == 0){
            console.log(input.val());
            if(input.val() != ''){
                $('.list-box').append('<div class="item">' + toAdd + '</div>');
                $('.no-item').remove();
                input.val('');
                count++;
                console.log(count);
            }
        }else{
            if(input.val() != ''){
                $('.list-box').append('<div class="item">' + toAdd + '</div>');
                input.val('');
                count++
                console.log(count);
            }
        }
    });

    $(document).on('mouseenter', 'div.item', function(){
        $(this).addClass('selected');
        $(this).append('<div class="remove">Remove</div>');
    });

    $(document).on('mouseleave', 'div.item', function(){
        $(this).removeClass('selected');
        $(this).children('.remove').remove();
    });

    $(document).on('mouseenter', 'div.remove', function(){
        $(this).toggleClass('remove-hover');
    });


    $(document).on('click', 'div.remove', function(){
        $(this).parent().remove();
            count--;
            console.log(count);
            if(count == 0){
                $('.list-box').append('<div class="no-item"><p>There is not items in your list<p/></div>');
            }
    });

    $(document).on('mouseleave', 'div.remove', function(){
        $(this).toggleClass('remove-hover');
    });


});
    
