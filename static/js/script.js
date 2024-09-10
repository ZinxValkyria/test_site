// Handle task selection
function handleTaskChange() {
    const taskSelect = document.getElementById('task');
    const customFlow = document.getElementById('custom_flow');
    const deploy_to = document.getElementById('deploy');


    // Show or hide custom workflow fields based on the selected task
    if (taskSelect.value === 'custom') {
        customFlow.style.display = 'block';  // Show custom workflow options
        }
        else if (taskSelect.value === 'deploy') {
            deploy_to.style.display = 'block';
            handledeploy();
        }
        else {
        customFlow.style.display = 'none';   // Hide custom workflow options
        // Fetch YAML from the local server for predefined tasks
        fetchFromLocal(taskSelect.value);
    }
}

// Handle task selection
function handledeploy() {
   


    // Show or hide custom workflow fields based on the selected task
    if (deploy_to.value === 'aws') {
            const url = `/fetch_yaml/deploy_to_aws.yaml`;
        }
        else if (deploy_to.value === 'gcp') {
            const url = `/fetch_yaml/deploy_to_aws.yaml`;
        }
        else if (deploy_to.value === 'azure') {
            const url = `/fetch_yaml/deploy_to_azure.yaml`;
        }
        else if (deploy_to.value === 'gh_pages') {
            const url = `/fetch_yaml/deploy_to_ghpages.yaml`;
        }
        else {
        customFlow.style.display = 'none';   // Hide custom workflow options
        // Fetch YAML from the local server for predefined tasks
        fetchFromLocal(taskSelect.value);
    }
}
// Fetch the YAML script from the local folder
function fetchFromLocal(task) {
    const url = `/fetch_yaml/${task}.yaml`;
    console.log(`Fetching ${url}...`);

    fetch(url)
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok: ' + response.statusText);
            }
            return response.text();
        })
        .then(script => {
            console.log("YAML Script:", script);
            // Display the fetched script in the output area
            document.getElementById('scriptOutput').textContent = script;
        })
        .catch(error => {
            console.error('Error fetching YAML script:', error);
            document.getElementById('scriptOutput').textContent = 'Error fetching YAML script.';
        });
}

function fetchFromLocal(task_deploy) {
    const url = `/fetch_yaml/${task_deploy}.yaml`;
    console.log(`Fetching ${url}...`);

    fetch(url)
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok: ' + response.statusText);
            }
            return response.text();
        })
        .then(script => {
            console.log("YAML Script:", script);
            // Display the fetched script in the output area
            document.getElementById('scriptOutput').textContent = script;
        })
        .catch(error => {
            console.error('Error fetching YAML script:', error);
            document.getElementById('scriptOutput').textContent = 'Error fetching YAML script.';
        });
}

// Add event listener for task selection change
document.getElementById('task').addEventListener('change', handleTaskChange);
