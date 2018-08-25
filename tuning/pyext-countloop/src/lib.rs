#[macro_use]

extern crate cpython;
extern crate ramp;
use cpython::{PyResult, Python};
use ramp::Int;

fn countloop_rust(_py: Python, times: &str) -> PyResult<u64> {
    let mut resp = Int::from(0);
    let loops: usize = times.parse::<usize>().unwrap();
    //println!("loops: {}", loops);

    for i in 0..loops {
        for x in 0..i {
            let a = Int::from(x).pow(i);
            resp = a % 5;
        }
    }

    Ok(u64::from(&resp))
}

py_module_initializer!(countloop, initcountloop, PyInit_countloop, |py, m| {
    try!(m.add(py, "__doc__", "This module is implemented in Rust"));
    try!(m.add(py, "countloop", py_fn!(py, countloop_rust(val: &str))));
    Ok(())
});