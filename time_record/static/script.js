
$('#time_submit').click(function(){
    var datetime_ary = Array();
    var act_ary = Array();  

    // Datetime - ['date','start_hr','start_min','end_hr','end_min']
    datetime_ary = datetime_ary.concat($('[id^="datepicker"]').map(function(){
        return this.value
    }).get());
    datetime_ary =  datetime_ary.concat($('[id^="Select_hr_1"]').map(function(){
        return this.value
    }).get());
    datetime_ary = datetime_ary.concat($('[id^="Select_min_1"]').map(function(){
        return this.value
    }).get());
    datetime_ary = datetime_ary.concat($('[id^="Select_hr_2"]').map(function(){
        return this.value
    }).get());
    datetime_ary = datetime_ary.concat($('[id^="Select_min_2"]').map(function(){
        return this.value
    }).get());
    
    // Action - ['act_type_1','act_type_2','act_name','act_note']
    act_ary = act_ary.concat($('[id^="act_type_1"]').map(function(){
        return this.value
    }).get());
    act_ary = act_ary.concat($('[id^="act_type_2"]').map(function(){
        return this.value
    }).get());
    act_ary = act_ary.concat($('[id^="act_name"]').map(function(){
        return this.value
    }).get());
    act_ary = act_ary.concat($('[id^="act_note"]').map(function(){
        return this.value
    }).get());

    // jQuery post(URL,data,function(data,status,xhr),dataType) 
    var post_all = $.post(
        'http://127.0.0.1:8000/update_mapping/',
        {
            'start_date_ary[]' : start_date_ary,
            'key_of_output_path[]' : output_path_arr,
        },);
    // jQuery.when() 
    $.when(post_all).done(function(){
        // https://ithelp.ithome.com.tw/articles/10242483
        window.location.href="http://127.0.0.1:8000/"
    });
});



$('#kcal_submit').click(function(){
    var datetime_ary = Array();
    var act_ary = Array();  

    // Datetime - ['date','start_hr','start_min','end_hr','end_min']
    datetime_ary = datetime_ary.concat($('[id^="datepicker"]').map(function(){
        return this.value
    }).get());
    datetime_ary =  datetime_ary.concat($('[id^="Select_hr_1"]').map(function(){
        return this.value
    }).get());
    datetime_ary = datetime_ary.concat($('[id^="Select_min_1"]').map(function(){
        return this.value
    }).get());
    datetime_ary = datetime_ary.concat($('[id^="Select_hr_2"]').map(function(){
        return this.value
    }).get());
    datetime_ary = datetime_ary.concat($('[id^="Select_min_2"]').map(function(){
        return this.value
    }).get());
    
    // Action - ['act_type_1','act_type_2','act_name','act_note']
    act_ary = act_ary.concat($('[id^="act_type_1"]').map(function(){
        return this.value
    }).get());
    act_ary = act_ary.concat($('[id^="act_type_2"]').map(function(){
        return this.value
    }).get());
    act_ary = act_ary.concat($('[id^="act_name"]').map(function(){
        return this.value
    }).get());
    act_ary = act_ary.concat($('[id^="act_note"]').map(function(){
        return this.value
    }).get());

    // jQuery post(URL,data,function(data,status,xhr),dataType) 
    var post_all = $.post(
        'http://127.0.0.1:8000/update_mapping/',
        {
            'start_date_ary[]' : start_date_ary,
            'key_of_output_path[]' : output_path_arr,
        },);
    // jQuery.when() 
    $.when(post_all).done(function(){
        // https://ithelp.ithome.com.tw/articles/10242483
        window.location.href="http://127.0.0.1:8000/"
    });
});