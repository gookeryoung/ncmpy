use std::env;
use pyo3::prelude::*;

/// ncmdump function
// #[pyfunction]
// fn ncm_dump(src_path: &str, dst_path: &str) -> Result<(), Error> {
//     use std::io::Write;
//     let file = File::open(src_path)?;
//     let mut ncm = Ncmdump::from_reader(file)?;
//     let music = ncm.get_data()?;
//     let mut target = File::options()
//         .create(true)
//         .write(true)
//         .open(dst_path)?;
//     target.write_all(&music)?;
//     Ok(())
// }
#[pyfunction]
fn double(x: usize) -> usize {
    x * 2
}

#[pyfunction]
fn print_cli_args(py: Python) -> PyResult<()> {
    // This one includes python and the name of the wrapper script itself, e.g.
    // `["/home/ferris/.venv/bin/python", "/home/ferris/.venv/bin/print_cli_args", "a", "b", "c"]`
    println!("{:?}", env::args().collect::<Vec<_>>());
    // This one includes only the name of the wrapper script itself, e.g.
    // `["/home/ferris/.venv/bin/print_cli_args", "a", "b", "c"])`
    println!(
        "{:?}",
        py.import("sys")?
            .getattr("argv")?
            .extract::<Vec<String>>()?
    );
    Ok(())
}

/// A Python module implemented in Rust.
#[pymodule]
fn libncmdump(_py: Python, m: &PyModule) -> PyResult<()> {
    // m.add_function(wrap_pyfunction!(ncm_dump, m)?)?;
    m.add_function(wrap_pyfunction!(double, m)?)?;
    m.add_function(wrap_pyfunction!(print_cli_args, m)?)?;
    Ok(())
}
