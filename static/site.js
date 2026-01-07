(function () {
    // Force currency codes to be uppercase A–Z only, max 3 chars
    document.querySelectorAll(".fx-code").forEach((el) => {
      el.addEventListener("input", () => {
        el.value = el.value.toUpperCase().replace(/[^A-Z]/g, "").slice(0, 3);
      });
    });
  
    // Clean amount input slightly (allow digits, commas, dot)
    const amount = document.getElementById("amount");
    if (amount) {
      amount.addEventListener("input", () => {
        amount.value = amount.value.replace(/[^\d.,]/g, "");
      });
    }
  })();