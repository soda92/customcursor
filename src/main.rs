fn main() {
    // Read an ICO file from disk:
    let file = std::fs::File::open("Cursors/aero_arrow.cur").unwrap();
    let icon_dir = ico::IconDir::read(file).unwrap();
    // Print the size of each image in the ICO file:
    for entry in icon_dir.entries() {
        println!("{}x{}", entry.width(), entry.height());
    }
    // Decode the first entry into an image:
    let image = icon_dir.entries()[0].decode().unwrap();
    // You can get raw RGBA pixel data to pass to another image library:
    let rgba = image.rgba_data();
    assert_eq!(rgba.len(), (4 * image.width() * image.height()) as usize);
    // Alternatively, you can save the image as a PNG file:
    let file = std::fs::File::create("icon.png").unwrap();
    image.write_png(file).unwrap();
}
