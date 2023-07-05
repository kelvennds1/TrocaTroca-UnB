from flask import Blueprint, redirect, session

logout_bp = Blueprint('logout', __name__)

@logout_bp.route('/logout')
def logout():
    # Remova as informações do usuário da sessão
    session.pop('user_id', None)
    session.pop('username', None)
    # Redirecione para a página de login
    return redirect('/login')
