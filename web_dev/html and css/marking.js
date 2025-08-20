function getGrade(marks){
    if(marks >= 90) return 'A+';
    else if(marks >= 80) return 'A';
    else if(marks >= 70) return 'B';
    else if(marks >= 60) return 'C';
    else if(marks >= 50) return 'D';
    else return 'F';
}
function calculateRowTotal(element) {
    let row = element.parentElement.parentElement;
    let cie = parseFloat(row.querySelector(".cie").value) || 0;
    let sce = parseFloat(row.querySelector(".sce").value) || 0;
    let ha = parseFloat(row.querySelector(".ha").value) || 0;
    let ese = parseFloat(row.querySelector(".ese").value) || 0;

    let total = cie + sce + ha + ese;
    row.querySelector(".rowTotal").textContent = total;

    let grade = getGrade(total);
    row.querySelector(".rowGrade").textContent = grade;


}

function calculateTotal() {
    let totalMarks = 0;
    let rowTotals = document.querySelectorAll(".rowTotal");

    rowTotals.forEach(cell => {
        totalMarks += parseInt(cell.textContent);
    });

    let percentage = (totalMarks / 500) * 100;

    document.getElementById("totalMarks").textContent = totalMarks;
    document.getElementById("percentage").textContent = percentage.toFixed(2);
}
