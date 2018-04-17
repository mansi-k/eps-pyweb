
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

