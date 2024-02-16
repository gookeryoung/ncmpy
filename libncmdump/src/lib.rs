use pyo3::prelude::*;
use anyhow::Result;
use ncmdump::Ncmdump;

use std::fs::File;
use std::path::Path;

/// ncmdump function
#[pyfunction]
fn ncm_dump(src_path: &str, dst_path: &str) -> PyResult<()> {
    use std::io::Write;
    let file = File::open(src_path)?;
    let mut ncm = Ncmdump::from_reader(file)?;
    let music = ncm.get_data()?;
    let mut target = File::options()
        .create(true)
        .write(true)
        .open(dst_path)?;
    target.write_all(&music)?;
    Ok(())
}

/// A Python module implemented in Rust.
#[pymodule]
fn libncmdump(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(ncm_dump, m)?)?;
    Ok(())
}
