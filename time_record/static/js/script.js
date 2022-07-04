
function changeOptions() {
    let act_type_main = document.getElementById("act_type_main").value;
    let id = `options-${act_type_main}`;
    let act_type_sub = document.getElementById("act_type_sub");
    for (let optgroup of act_type_sub.children) {
        let match = optgroup.id === id;
        optgroup[(match ? "remove" : "set") + "Attribute"]("hidden", "hidden");
        if (match) {
            act_type_sub.value = optgroup.children[0].value;
        }
    }
}
changeOptions();

// Auto today
var date = new Date();
var day = date.getDate();
var month = date.getMonth() + 1;
var year = date.getFullYear();
if (month < 10) month = "0" + month;
if (day < 10) day = "0" + day;
var today = year + "-" + month + "-" + day;
document.getElementById("startdateId").value = today;
document.getElementById("cal_date").value = document.getElementById("startdateId").value;



var date = new Date();
var day = date.getDate();
var month = date.getMonth() + 1;
var year = date.getFullYear();
if (month < 10) month = "0" + month;
if (day < 10) day = "0" + day;
var today = year + "-" + month + "-" + day;
document.getElementById("startdateId").value = today;


function calAutoToday() {   
    document.getElementById("cal_date").value = document.getElementById("startdateId").value;
}
calAutoToday();


// Auto calculated input value with javascript & oninput Event
function autoCaculate() {   
    var cal_MRNG = document.getElementById('cal_MRNG').value;
    var cal_NOON = document.getElementById('cal_NOON').value; 
    var cal_NIGHT = document.getElementById('cal_NIGHT').value; 
    var cal_TARGET = document.getElementById('cal_TARGET').value; 
    document.getElementById('cal_DEFICITE').value = (cal_TARGET-cal_NIGHT-cal_NOON-cal_MRNG);
}
autoCaculate();

