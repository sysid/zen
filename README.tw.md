# ZEN TW
## Python
create virtualenv in GITROOT
cd /Users/Q187392/dev/s/forked/zen/bindings/python
maturin develop (create + install whl)
python index.py

compiling `cargo build` in GITROOT does not work

## Rust


## V8
handler/function/scripts contains libs and global overwrites for V8, e.g. `console.log`
`v8::Isolate::CreateParams` contains the `ArrayBufferAllocator` which is used for memory allocation
console.log will be captured in Trace-Object as: `trace_data: Some(Object {"log": Array [Object {"lines": Array [String("{\"input\":15}")], "msSinceRun": Number(0)}]})`

cargo test --package zen-engine --lib handler::graph::tests::function -- --exact
