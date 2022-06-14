


$('#Select_Date_Submit').click(function(){
    var end_date_ary = Array();  
    var start_date_ary = Array();

    start_date_ary.push($('[id^="Select_Year_1"]').map(function(){
        return this.value
    }).get());

    start_date_ary.push($('[id^="Select_Month_1"]').map(function(){
        return this.value
    }).get());


    // var data_for_post_ = {
    //     'start_date_ary[]' : start_date_ary,
    //     // 'key_of_output_path[]' : output_path_arr,
    // };
    


    // var post_update_data = $.post('http://127.0.0.1:8000/update_mapping/', data_for_post_);
    // var post_mapping_triger = $.post('http://127.0.0.1:8000/select_to_excel/');
         // redirect current page
    // $.when(post_checked_data).done(function(){
    //     window.location.href="http://127.0.0.1:8000/"
    });
    