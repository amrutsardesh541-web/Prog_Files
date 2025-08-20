function divide(a, b) {
    try {
      if (b === 0) {
        throw new Error("Cannot divide by zero");
      }
      let result = a / b;
      console.log("Result:", result);
    } catch (error) {
      console.log("Error:", error.message);
    } finally {
      console.log("Division operation completed.");
    }
  }
  
  divide(10, 2);   // Valid
  divide(5, 0);    // Triggers error
  