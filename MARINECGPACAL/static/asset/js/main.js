function create_tr(table_id) {
    let table_body = document.getElementById(table_id),
        first_tr   = table_body.firstElementChild
        tr_clone   = first_tr.cloneNode(true);

    table_body.append(tr_clone);

    clean_first_tr(table_body.firstElementChild);
}

function clean_first_tr(firstTr) {
    let children = firstTr.children;
    
    children = Array.isArray(children) ? children : Object.values(children);
    children.forEach(x=>{
        if(x !== firstTr.lastElementChild)
        {
            x.firstElementChild.value = '';
        }
    });
}



function remove_tr(This) {
    if(This.closest('tbody').childElementCount == 1)
    {
        alert("You Don't have Permission to Delete This ?");
    }else{
        This.closest('tr').remove();
    }
}

function create_tr2(table_id) {
    let table_body2 = document.getElementById(table_id),
        first_tr2   = table_body.firstElementChild
        tr_clone2   = first_tr2.cloneNode(true);

    table_body2.append(tr_clone2);

    clean_first_tr(table_body2.firstElementChild);
}

function clean_first_tr2(firstTr2) {
    let children2 = firstTr2.children;
    
    children2 = Array.isArray(children2) ? children2 : Object.values(children2);
    children2.forEach(x=>{
        if(x !== firstTr2.lastElementChild)
        {
            x.firstElementChild.value = '';
        }
    });
}



function remove_tr2(This) {
    if(This.closest('tbody2').childElementCount == 1)
    {
        alert("You Don't have Permission to Delete This ?");
    }else{
        This.closest('tr').remove();
    }
}





function addUpCreditsGpa() {
    const creditUnit = document.querySelectorAll('[name = creditUnit]');
    const grade = document.querySelectorAll('[name = grade]');
    let totalUnit = document.querySelector("[name = totalUnit]").value = "";
    let gpa = document.querySelector("[name = gpa]").value = "";
    let option1 = "";
    let option2 = "";
    let a  = [];
    for (let i = 0; i < creditUnit.length; ++i) {
        option1 = creditUnit[i].options[creditUnit[i].selectedIndex].text;
        let totalUnit = document.querySelector("[name = totalUnit]").value;
        totalUnit = Number(totalUnit) + Number(option1);
        a.push(totalUnit);
    }
    let asum = a.reduce((partial_sum, a) => partial_sum + a,0); 

    let b = [];
    for (let i = 0; i < grade.length; ++i) {
        option2 = grade[i].options[grade[i].selectedIndex].text;
        let gpa = document.querySelector("[name = gpa]").value;
        let letterPoint = gradeToPoints(option2);
        let totalPoint = letterPoint;
        b.push(totalPoint);
    }
    let addAB = a.reduce(function(r,a,i){return r+a*b[i]},0);
    

    let gpaScore = parseFloat(addAB / asum).toFixed(2);
    document.querySelector("[name = totalUnit]").value = asum;
    document.querySelector("[name = gpa]").value = gpaScore;
}

//Return the points corresponding to the given letter
function gradeToPoints(grade) {   
    if ("A" == grade) {
        return 5.0;
    }
    else if ("B" == grade) {
        return 4.0;
    }
    else if ("C" == grade) {
        return 3.0;
    }
    else if ("D" == grade) {
        return 2.0;
    }
    else if ("E" == grade) {
        return 1.0;
    }
    else if ("F" == grade) {
        return 0.0;
    }
    else {
        //Guess we should we throw an exception here?
        return Invalid;
    }
}