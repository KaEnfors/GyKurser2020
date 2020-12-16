

console.log("Hej!??");
var count = 0;
console.log("count is: " +  count);




function btnClick() {
    console.log("You clicked the button " + count + " times!");
    count++;
}

function btnBgChange() {
    if (document.body.style.backgroundColor == 'blue')
        document.body.style.backgroundColor = 'red';
    else
        document.body.style.backgroundColor = 'blue';

}
