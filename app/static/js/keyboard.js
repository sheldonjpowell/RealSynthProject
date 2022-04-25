const audioContext = new (window.AudioContext || window.webkitAudioContext)();

const getElementByNote = (note) =>
  note && document.querySelector(`[note="${note}"]`);
  


const keys = {
    A: { element: getElementByNote("C"), note: "C", octaveOffset: 0 },
    W: { element: getElementByNote("C#"), note: "C#", octaveOffset: 0 },
    S: { element: getElementByNote("D"), note: "D", octaveOffset: 0 },
    E: { element: getElementByNote("D#"), note: "D#", octaveOffset: 0 },
    D: { element: getElementByNote("E"), note: "E", octaveOffset: 0 },
    F: { element: getElementByNote("F"), note: "F", octaveOffset: 0 },
    T: { element: getElementByNote("F#"), note: "F#", octaveOffset: 0 },
    G: { element: getElementByNote("G"), note: "G", octaveOffset: 0 },
    Y: { element: getElementByNote("G#"), note: "G#", octaveOffset: 0 },
    H: { element: getElementByNote("A"), note: "A", octaveOffset: 1 },
    U: { element: getElementByNote("A#"), note: "A#", octaveOffset: 1 },
    J: { element: getElementByNote("B"), note: "B", octaveOffset: 1 },
    K: { element: getElementByNote("C2"), note: "C", octaveOffset: 1 },
    O: { element: getElementByNote("C#2"), note: "C#", octaveOffset: 1 },
    L: { element: getElementByNote("D2"), note: "D", octaveOffset: 1 },
    P: { element: getElementByNote("D#2"), note: "D#", octaveOffset: 1 },
    semicolon: { element: getElementByNote("E2"), note: "E", octaveOffset: 1 }
  };

  const getHz = (note = "A", octave = 4) => {
    const A4 = 440;

    
    //Grabbing Octave slider from Index
    let octSlider = document.querySelector('input[className="octSlider"').value;
    octSlider = parseFloat(octSlider)





    let N = 0;
    switch (note) {
      default:
      case "A":
        N = 0;
        break;
      case "A#":
      case "Bb":
        N = 1;
        break;
      case "B":
        N = 2;
        break;
      case "C":
        N = 3;
        break;
      case "C#":
      case "Db":
        N = 4;
        break;
      case "D":
        N = 5;
        break;
      case "D#":
      case "Eb":
        N = 6;
        break;
      case "E":
        N = 7;
        break;
      case "F":
        N = 8;
        break;
      case "F#":
      case "Gb":
        N = 9;
        break;
      case "G":
        N = 10;
        break;
      case "G#":
      case "Ab":
        N = 11;
        break;
    }

    N += 12 * (octave - (octSlider + 3));
    console.log(`Note: ${note}`)
    return A4 * Math.pow(2, N / 12);
};


const pressedNotes = new Map();
let clickedKey = "";





const playKey = (key) => {
    if (!keys[key]) {
      return;
    }



    let volumeSlider = document.querySelector('input[className="volumeSlider"').value;
    volumeSlider = parseFloat(volumeSlider)
    console.log(`${volumeSlider}`)

    let attackSlider = document.querySelector('input[className="attackSlider"').value;
    attackSlider = parseFloat(attackSlider)
    console.log(`${attackSlider}`)

    let decaySlider = document.querySelector('input[className="decaySlider"').value;
    decaySlider = parseFloat(decaySlider)
    console.log(`${decaySlider}`)

    let sustainSlider = document.querySelector('input[className="sustainSlider"').value;
    sustainSlider = parseFloat(sustainSlider)
    console.log(sustainSlider)


    let releaseSlider = document.querySelector('input[className="releaseSlider"').value;
    releaseSlider = parseFloat(releaseSlider)
    console.log(`${releaseSlider}`)


    
    const osc = audioContext.createOscillator();
    const noteGainNode = audioContext.createGain();
    
    noteGainNode.connect(audioContext.destination);
    console.log(`currentTime${audioContext.currentTime}`)


    const zeroGain = 0.000001;
    const maxGain = volumeSlider;
    const sustainedGain = 0.0001;
    noteGainNode.gain.value = zeroGain;
  
    const setAttack = () =>
    noteGainNode.gain.exponentialRampToValueAtTime(
      maxGain,
      audioContext.currentTime + attackSlider 
    );
      
    const setDecay = () =>
        noteGainNode.gain.linearRampToValueAtTime(
          sustainedGain,
            audioContext.currentTime + decaySlider
        );
    // const setSustain = () =>
    //   noteGainNode.gain.linearRampToValueAtTime(
    //     // maxGain,
    //     sustainedGain,
    //     audioContext.currentTime + sustainSlider
    //   );
    const setRelease = () =>
        noteGainNode.gain.linearRampToValueAtTime(
            zeroGain,
            audioContext.currentTime + releaseSlider
            
            );

    // let pulseTime = 1;
    // function playPulse(time) {
    //     let lfoHz = document.querySelector('#lfo').value;
    //     lfoHz = parseFloat(lfoHz)
    //     // let osc = audioContext.createOscillator();
    //     // osc.type = 'sine';
    //     // osc.frequency.value = pulseHz;

    //     let amp = audioContext.createGain();
    //     amp.gain.value = 1;

    //     let lfo = audioContext.createOscillator();
    //     lfo.type = 'square';
    //     lfo.frequency.value = lfoHz;

    //     lfo.connect(amp.gain);
    //     osc.connect(amp).connect(audioContext.destination);
    //     // lfo.start();a
    //     // osc.start(time);
    //     // osc.stop(pulseTime);
    // }
  
    setAttack();
    setDecay();
    setRelease();
    // setSustain();
    // setVolume();

    // playPulse()
    
      




    /////////////////////////////////////////////////////////
    /////////////////////////////////////////////////////////
    /////////////////////////////////////////////////////////
    /////////////////////////////////////////////////////////

    
    

    
    
    ///// This is the Waveform.js Connection/////

    osc.connect(noteGainNode);
    let inputSlider = document.querySelector('input[className="waveSlider"').value;
    console.log(inputSlider)
    osc.type = WAVEFORMS[inputSlider]

    
    
    // osc.type = "triangle";
  
    const freq = getHz(keys[key].note, (keys[key].octaveOffset || 0) + 3);
    console.log(`Freq: ${freq}`)
  
    if (Number.isFinite(freq)) {
      osc.frequency.value = freq;
    }
  
    keys[key].element.classList.add("pressed");
    pressedNotes.set(key, osc);
    pressedNotes.get(key).start();
  };

const stopKey = (key) => {
    if (!keys[key]) {
      return;
    }
    
    keys[key].element.classList.remove("pressed");
    const osc = pressedNotes.get(key);
  
    if (osc) {
  

      let sustainSlider = document.querySelector('input[className="sustainSlider"').value;
      sustainSlider = parseFloat(sustainSlider)
      console.log(sustainSlider)
      
      setTimeout(() => {
        osc.stop();
      }, sustainSlider);
  
      pressedNotes.delete(key);
    }
  };




/////////////////////////////////////////////
/////////////////////////////////////////////
/////////////////////////////////////////////







/////////////////////////////////////////////////////////
/////////////////////////////////////////////////////////
        /////THIS IS WHERE I ADD THE MIDI///////
/////////////////////////////////////////////////////////
/////////////////////////////////////////////////////////







const oscillators = {};

function midiToFreq(number) {
    
    const A4 = 440;
    return (A4/ 32) * (2 ** ((number- 9) / 12));
}

if (navigator.requestMIDIAccess) {
    navigator.requestMIDIAccess().then(success, failure)
}

function success(midiAccess) {
    midiAccess.addEventListener('statechange', updateDevices);

    const inputs = midiAccess.inputs;
    
    inputs.forEach((input) =>{
        input.addEventListener('midimessage', handleInput)
    })
}



function handleInput(input){
    const command = input.data[0];
    const note = input.data[1];
    const velocity = input.data[2];

    switch (command){
        case 144:
        if(velocity > 0){
            // note on
            noteOn(note, velocity);
        } else {
            noteOff(note);
        }
        break;
        case 128:
        noteOff(note);
            break; // note off
    }    
}




//// NOTE ON MIDI //////

function noteOn(note, velocity){


    let volumeSlider = document.querySelector('input[className="volumeSlider"').value;
    volumeSlider = parseFloat(volumeSlider)
    console.log(`${volumeSlider}`)

    let attackSlider = document.querySelector('input[className="attackSlider"').value;
    attackSlider = parseFloat(attackSlider)
    console.log(`${attackSlider}`)

    let decaySlider = document.querySelector('input[className="decaySlider"').value;
    decaySlider = parseFloat(decaySlider)
    console.log(`${decaySlider}`)

    let sustainSlider = document.querySelector('input[className="sustainSlider"').value;
    sustainSlider = parseFloat(sustainSlider)
    console.log(sustainSlider)


    let releaseSlider = document.querySelector('input[className="releaseSlider"').value;
    releaseSlider = parseFloat(releaseSlider)
    console.log(`${releaseSlider}`)



    let inputSlider = document.querySelector('input[className="waveSlider"').value;

    const osc = audioContext.createOscillator();

    const oscGain = audioContext.createGain()
    oscGain.gain.value = .33;
    const velocityGainAmount = (1 / 127) * velocity;
    const velocityGain = audioContext.createGain();
    velocityGain.gain.value = velocityGainAmount;
    // connecting the WaveFroms to The Midi Controler
    osc.type = WAVEFORMS[inputSlider];
    osc.frequency.value = midiToFreq(note);


    oscGain.connect(audioContext.destination);
    console.log(`currentTime${audioContext.currentTime}`)


    const zeroGain = 0.000001;
    const maxGain = volumeSlider;
    const sustainedGain = 0.0001;
    oscGain.gain.value = zeroGain;
  
    const setAttack = () =>
    oscGain.gain.exponentialRampToValueAtTime(
      maxGain,
      audioContext.currentTime + attackSlider 
    );
      
    const setDecay = () =>
        oscGain.gain.linearRampToValueAtTime(
          sustainedGain,
            audioContext.currentTime + decaySlider
        );

    const setRelease = () =>
        oscGain.gain.linearRampToValueAtTime(
            zeroGain,
            audioContext.currentTime + releaseSlider
            
            );


    
    console.log(WAVEFORMS[inputSlider])
    console.log(osc.type)
    console.log(note)
    console.log(`NoteOn: ${osc.frequency.value}`)



    osc.connect(oscGain);
    oscGain.connect(velocityGain);
    velocityGain.connect(audioContext.destination);

    osc.gain = oscGain;
    oscillators[note.toString()] = osc;
    console.log(oscillators[note.toString()])


    osc.start();

    setAttack();
    setDecay();
    setRelease();
}




////// NOTE OFF MIDI////////

function noteOff(note){
    const osc = oscillators[note.toString()];
    const oscGain = osc.gain;
    oscGain.gain.setValueAtTime(oscGain.gain.value, audioContext.currentTime);
    oscGain.gain.exponentialRampToValueAtTime(0.0001, audioContext.currentTime + 0.03);

    let sustainSlider = document.querySelector('input[className="sustainSlider"').value;
      sustainSlider = parseFloat(sustainSlider)
      console.log(sustainSlider)
      
      setTimeout(() => {
        osc.stop();
        // osc.disconnect();
      }, sustainSlider);
    // osc.stop();

    delete oscillators[note.toString()];
    // console.log(oscillators)

}


function updateDevices(event){
    console.log(`Name: ${event.port.name}, Brand: ${event.port.manufacturer}, State: ${event.port.state}, Type: ${event.port.type}`)

}

function failure() {
    console.log('Could not connect MIDI')
}





// /////////////////////////////////////////////
// /////////////////////////////////////////////
// /////////////////////////////////////////////
// /////////////////////////////////////////////
// /////////////////////////////////////////////














document.addEventListener("keydown", (e) => {
    const eventKey = e.key.toUpperCase();
    const key = eventKey === ";" ? "semicolon" : eventKey;
    
    if (!key || pressedNotes.get(key)) {
      return;
    }
    playKey(key);
  });
  
  document.addEventListener("keyup", (e) => {
    const eventKey = e.key.toUpperCase();
    const key = eventKey === ";" ? "semicolon" : eventKey;
    
    if (!key) {
      return;
    }
    stopKey(key);
  });
  
  for (const [key, { element }] of Object.entries(keys)) {
    element.addEventListener("mousedown", () => {
      playKey(key);
      clickedKey = key;
    });
  }
  
  document.addEventListener("mouseup", () => {
    stopKey(clickedKey);
  });


/////////////////////////////////////////////
/////////////////////////////////////////////
/////////////////////////////////////////////


const presets = {
    

}




  