javascript: function % 20rlrd() {
    var % 20d = document,
    z = d.createElement('scr' + 'ipt'),
    b = d.body;
    try {
        if (!b) throw (0);
        d.title = '(Saving...)%20' + d.title;
        z.setAttribute('src', 'http://localhost:5000/save/-1?url=' + encodeURIComponent(d.location.href) + '&headline="test"&desc="saddas"');
        b.appendChild(z);
    } catch(e) {
        alert('Please%20wait%20until%20the%20page%20has%20loaded.');
    }
}
rlrd();
void(0)