const output = document.getElementById("output");

document.getElementById("loadFrames").addEventListener("click", () => {
    output.textContent = "Loading frames from assets folder...";
    // Here we will eventually call Rust backend to actually load frames
});

document.getElementById("annotateFrame").addEventListener("click", () => {
    output.textContent = "Annotating a frame...";
    // Here we will eventually call Rust backend to save annotation
});
