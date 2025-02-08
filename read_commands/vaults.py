from fastapi import APIRouter
import subprocess

router = APIRouter()

def run_command(args: list):
    """
    Ejecuta el comando 'python3 symb.py' con los argumentos dados y retorna el resultado.
    """
    try:
        result = subprocess.run(
            ["python3", "symb.py"] + args,
            capture_output=True,
            text=True
        )
        output = result.stdout.strip()
        error = result.stderr.strip()
        return {"output": output, "error": error if error else None}
    except Exception as e:
        return {"error": str(e)}

@router.get("/isvault/{address}", tags=["Read Commands - Related to Vaults"])
def isvault(address: str):
    """
    Check if address is vault.
    """
    return run_command(["isvault", address])

@router.get("/vaults", tags=["Read Commands - Related to Vaults"])
def vaults():
    """
    List all vaults.
    """
    return run_command(["vaults"])

@router.get("/vaultnets/{vault_address}", tags=["Read Commands - Related to Vaults"])
def vaultnets(vault_address: str):
    """
    List all networks associated with the given vault.
    """
    return run_command(["vaultnets", vault_address])

@router.get("/vaultops/{vault_address}", tags=["Read Commands - Related to Vaults"])
def vaultops(vault_address: str):
    """
    List all operators opted into the given vault.
    """
    return run_command(["vaultops", vault_address])

@router.get("/vaultnetsops/{vault_address}", tags=["Read Commands - Related to Vaults"])
def vaultnetsops(vault_address: str):
    """
    List all operators and their associated networks for the given vault.
    """
    return run_command(["vaultnetsops", vault_address])
