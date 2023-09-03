document.addEventListener('DOMContentLoaded', () => {
    const audioElement = document.getElementById('audio');
    const audioContext = new (window.AudioContext || window.webkitAudioContext)();
    const analyser = audioContext.createAnalyser();
    
    const source = audioContext.createMediaElementSource(audioElement);
    source.connect(analyser);
    analyser.connect(audioContext.destination);
    
    analyser.fftSize = 256;
    const bufferLength = analyser.frequencyBinCount;
    const dataArray = new Uint8Array(bufferLength);
    
    const canvas = document.getElementById('visualizer');
    const canvasCtx = canvas.getContext('2d');
    
    function draw() {
      analyser.getByteFrequencyData(dataArray);
      const average = dataArray.reduce((acc, val) => acc + val, 0) / bufferLength;
      const scale = 1 + average / 256; // Adjust the scale based on audio intensity
      
      canvasCtx.clearRect(0, 0, canvas.width, canvas.height);
      
      const centerX = canvas.width / 2;
      const centerY = canvas.height / 2;
      const radius = 50 * scale; // Adjust the radius based on audio intensity
      
      canvasCtx.beginPath();
      canvasCtx.arc(centerX, centerY, radius, 0, 2 * Math.PI);
      canvasCtx.strokeStyle = '#333';
      canvasCtx.lineWidth = 2;
      canvasCtx.stroke();
      
      requestAnimationFrame(draw);
    }
    
    draw();
    
    audioElement.addEventListener('play', () => {
      if (audioContext.state === 'suspended') {
        audioContext.resume();
      }
    });
    
    audioElement.addEventListener('pause', () => {
      if (audioContext.state === 'running') {
        audioContext.suspend();
      }
    });
  });
  