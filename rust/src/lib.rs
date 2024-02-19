use std::fs::File;
use std::io::Write;

use ncmdump::Ncmdump;
use pyo3::prelude::*;

#[pyfunction]
#[pyo3(name = "ncmdump")]
fn ncm_dump(src_path: &str, dst_path: &str) -> PyResult<()> {
    let file = File::open(src_path).expect("无法打开文件");
    let mut ncm = Ncmdump::from_reader(file).unwrap();
    let music = ncm.get_data().unwrap();
    let target = File::options()
        .create(true)
        .write(true)
        .open(dst_path);
    target?.write_all(&music).unwrap();
    Ok(())
}

/// A Python module implemented in Rust.
#[pymodule]
fn libncmdump(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(ncm_dump, m)?)?;
    Ok(())
}
