function deleteNote() {
    var note = this.parentNode.parentNode.parentNode;
    note.parentNode.removeChild(note);
  }
  
  // Function to add a picture
  function addPicture() {
    var note = this.parentNode.parentNode.parentNode;
    var fileInput = document.createElement('input');
    fileInput.type = 'file';
    fileInput.accept = 'image/*';
    fileInput.addEventListener('change', function(event) {
      var file = event.target.files[0];
      var reader = new FileReader();
      reader.onload = function() {
        var image = document.createElement('img');
        image.src = reader.result;
        note.appendChild(image);
      };
      reader.readAsDataURL(file);
    });
    fileInput.click();
  }
  
  // Function to add a note
  function addNote() {
    var container = document.getElementsByClassName('container')[0];
    var note = document.createElement('div');
    note.className = 'note';
    var noteHeader = document.createElement('div');
    noteHeader.className = 'note-header';
    var noteTitle = document.createElement('h2');
    noteTitle.innerText = 'Note Title';
    var noteOptions = document.createElement('div');
    noteOptions.className = 'note-options';
    var addNoteBtn = document.createElement('button');
    addNoteBtn.className = 'add-note';
    addNoteBtn.innerHTML = '&#43';
    addNoteBtn.addEventListener('click', addNote);
    var addPictureBtn = document.createElement('button');
    addPictureBtn.className = 'add-picture';
    addPictureBtn.innerHTML = '&#128247';
    addPictureBtn.addEventListener('click', addPicture);
    var deleteNoteBtn = document.createElement('button');
    deleteNoteBtn.className = 'delete-note';
    deleteNoteBtn.innerHTML = '&#128465';
    deleteNoteBtn.addEventListener('click', deleteNote);
    var textarea = document.createElement('textarea');
  
    noteOptions.appendChild(addNoteBtn);
    noteOptions.appendChild(addPictureBtn);
    noteOptions.appendChild(deleteNoteBtn);
  
    noteHeader.appendChild(noteTitle);
    noteHeader.appendChild(noteOptions);
  
    note.appendChild(noteHeader);
    note.appendChild(textarea);
  
    container.appendChild(note);
  }
  
  // Add event listeners to existing buttons
  var deleteNoteButtons = document.getElementsByClassName('delete-note');
  for (var i = 0; i < deleteNoteButtons.length; i++) {
    deleteNoteButtons[i].addEventListener('click', deleteNote);
  }
  
  var addPictureButtons = document.getElementsByClassName('add-picture');
  for (var i = 0; i < addPictureButtons.length; i++) {
    addPictureButtons[i].addEventListener('click', addPicture);
  }
  
  var addNoteButton = document.getElementsByClassName('add-note')[0];
  addNoteButton.addEventListener('click', addNote);
  