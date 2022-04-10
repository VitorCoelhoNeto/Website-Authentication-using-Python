/**
 * Deletes a note from a user's note list
 * @param  {[int]} noteId Note ID fetched from the database (check home.html)
 */
function deleteNote(noteId)
{
    fetch('/delete-note', {
        method: 'POST',
        body: JSON.stringify({ noteId: noteId}),
    }).then((_res) => {
        window.location.href = "/";
    });
}