// Simple template system for shared header/footer
document.addEventListener('DOMContentLoaded', function() {
    // Load header
    const headerElement = document.querySelector('header[data-template="header"]');
    if (headerElement) {
        fetch('header.html')
            .then(response => {
                if (!response.ok) {
                    throw new Error('Template not found');
                }
                return response.text();
            })
            .then(html => {
                headerElement.outerHTML = html;
            })
            .catch(error => console.log('Header template not found, using existing content'));
    }
    
    // Load footer
    const footerElement = document.querySelector('footer[data-template="footer"]');
    if (footerElement) {
        fetch('footer.html')
            .then(response => {
                if (!response.ok) {
                    throw new Error('Template not found');
                }
                return response.text();
            })
            .then(html => {
                footerElement.outerHTML = html;
            })
            .catch(error => console.log('Footer template not found, using existing content'));
    }
});