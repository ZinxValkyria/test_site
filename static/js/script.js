document.addEventListener('DOMContentLoaded', function () {
    const stepTypeRadios = document.querySelectorAll('input[name="step_type"]');
    const customStepFields = document.getElementById('customStepFields');

    stepTypeRadios.forEach(radio => {
        radio.addEventListener('change', function () {
            if (this.value === 'custom') {
                customStepFields.style.display = 'block';
            } else {
                customStepFields.style.display = 'none';
            }
        });
    });
});
