from fastapi import FastAPI
import subprocess

app = FastAPI()

def run_command(args: list):
    try:
        result = subprocess.run(["python3", "symb.py"] + args, capture_output=True, text=True)
        return {"output": result.stdout.strip(), "error": result.stderr.strip()} if result.stderr else {"output": result.stdout.strip()}
    except Exception as e:
        return {"error": str(e)}

@app.get("/isnet/")
def isnet(address: str):
    return run_command(["isnet", address])

@app.get("/middleware/")
def middleware(network_address: str):
    return run_command(["middleware", network_address])

@app.get("/nets/")
def nets():
    return run_command(["nets"])

@app.get("/netops/")
def netops(network_address: str):
    return run_command(["netops", network_address])

@app.get("/netstakes/")
def netstakes(network_address: str):
    return run_command(["netstakes", network_address])

@app.get("/max-network-limit/")
def max_network_limit(vault_address: str, network_address: str):
    return run_command(["max-network-limit", vault_address, network_address])

@app.get("/network-limit/")
def network_limit(vault_address: str, network_address: str):
    return run_command(["network-limit", vault_address, network_address])

@app.get("/pending-resolver/")
def pending_resolver(vault_address: str, network_address: str):
    return run_command(["pending-resolver", vault_address, network_address])

@app.get("/resolver/")
def resolver(vault_address: str, network_address: str):
    return run_command(["resolver", vault_address, network_address])