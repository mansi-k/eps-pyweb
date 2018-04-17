
function cancelp(cexb){
    var rgid = cexb.value;
    var ans = confirm("Your registration for this event with registration ID "+rgid+" will be revoked")
    if(ans) {
        $.ajax({
            url: '/participate',
            data: JSON.stringify({'rgid':rgid}),
            type: 'POST',
            contentType: "application/json; charset=utf-8",
            dataType: "json",
            success: function(response){
                $("#partdiv").load(location.href + " #partdiv>*", "");
                if(response['status']=='ok')
                    alert("Participation Revoked")
                else
                    alert("Failed")
            },
            error: function(error){
                console.log(error);
            }
        });
    }
};

function cpart(cexb){
    var rgid = cexb.value;
    var ans = confirm("Your registration for this event with registration ID "+rgid+" will be revoked")
    if(ans) {
        $.ajax({
            url: '/participate',
            data: JSON.stringify({'rgid':rgid}),
            type: 'POST',
            contentType: "application/json; charset=utf-8",
            dataType: "json",
            success: function(response){
                $("#partdiv").load(location.href + " #partdiv>*", "");
                if(response['status']=='ok') {
                    $(cexb).closest('tr').remove();
                    alert("Participation Revoked");
                }
                else
                    alert("Failed")
            },
            error: function(error){
                console.log(error);
            }
        });
    }
};

function participatex(pexb){
    var usid = pexb.value;
    var ans = confirm("Confirm to participate")
    if(ans) {
        $.ajax({
            url: '/participate',
            data: JSON.stringify({'usid':usid}),
            type: 'POST',
            contentType: "application/json; charset=utf-8",
            dataType: "json",
            success: function(response){
                $("#partdiv").load(location.href + " #partdiv>*", "");
                if(response['status']=='ok')
                    alert("Participated")
                else
                    alert("Failed")
                //$('#partdiv').load(' #partdiv')
            },
            error: function(error){
                console.log(error);
            }
        });
    }
};

$(document).ready(function(){
    tabpast = 0;
    tabupg = 0;

    $('.nav-pills a').on('shown.bs.tab', function (e) {
        var target = $(e.target).attr("href") // activated tab
        var table = target+'table';
        var xf = target.substring(1,target.length);
        //alert(target);
        if(target=='#upcoming' && tabupg==0) {
            $.ajax({
                url: '/fxsearch',
                data: JSON.stringify({'xf':xf}),
                type: 'POST',
                contentType: "application/json; charset=utf-8",
                dataType: "json",
                success: function(response){
                    $.each(response, function(i, item) {
                        $(table).children('tbody').append("<tr><td>"+item.ex_name+"</td><td>"+item.cat_name+"</td><td>"+item.ex_city+"</td><td>"+item.ex_start_date.slice(0,-7)+"</td><td><a href=\"http://127.0.0.1:5000/details/"+item.ex_id+'|'+item.ex_city+"\" target='_blank'><button type='button' class='btn btn-primary'>View</button></a></td></tr>");
                    });
                },
                error: function(error){
                    console.log(error);
                }
            });
            tabupg=1;
        }
        else if(target=='#past' && tabpast==0) {
            $.ajax({
                url: '/fxsearch',
                data: JSON.stringify({'xf':xf}),
                type: 'POST',
                contentType: "application/json; charset=utf-8",
                dataType: "json",
                success: function(response){
                    $.each(response, function(i, item) {
                        $(table).children('tbody').append("<tr><td>"+item.ex_name+"</td><td>"+item.cat_name+"</td><td>"+item.ex_city+"</td><td>"+item.ex_start_date.slice(0,-7)+"</td><td><a href=\"http://127.0.0.1:5000/details/"+item.ex_id+'|'+item.ex_city+"\" target='_blank'><button type='button' class='btn btn-primary'>View</button></a></td></tr>");
                    });
                },
                error: function(error){
                    console.log(error);
                }
            });
            tabpast=1;
        }
    });
});




