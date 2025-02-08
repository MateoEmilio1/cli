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

@router.get("/active-balance-of/{vault_address}/{address}", tags=["Read Commands - Related to Stakers"])
def active_balance_of(vault_address: str, address: str):
    """
    Get an active balance of a given account at a particular vault.
    
    Command:
      python3 symb.py active-balance-of VAULT_ADDRESS ADDRESS
      
    VAULT_ADDRESS - an address of the vault.
    ADDRESS - an address to get an active balance for.
    """
    return run_command(["active-balance-of", vault_address, address])

@router.get("/withdrawals-of/{vault_address}/{epoch}/{address}", tags=["Read Commands - Related to Stakers"])
def withdrawals_of(vault_address: str, epoch: str, address: str):
    """
    Get some epoch’s withdrawals of a given account at a particular vault.
    
    Command:
      python3 symb.py withdrawals-of VAULT_ADDRESS EPOCH ADDRESS
      
    VAULT_ADDRESS - an address of the vault.
    EPOCH - an epoch to get withdrawals for.
    ADDRESS - an address to get withdrawals for.
    """
    return run_command(["withdrawals-of", vault_address, epoch, address])

@router.get("/withdrawals-claimed/{vault_address}/{epoch}/{address}", tags=["Read Commands - Related to Stakers"])
def withdrawals_claimed(vault_address: str, epoch: str, address: str):
    """
    Check if some epoch’s withdrawals of a given account at a particular vault are claimed.
    
    Command:
      python3 symb.py withdrawals-claimed VAULT_ADDRESS EPOCH ADDRESS
      
    VAULT_ADDRESS - an address of the vault.
    EPOCH - an epoch to check for.
    ADDRESS - an address to check if the withdrawals are claimed for.
    """
    return run_command(["withdrawals-claimed", vault_address, epoch, address])
