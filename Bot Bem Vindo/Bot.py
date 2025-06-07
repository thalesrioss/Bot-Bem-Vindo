print("Bot iniciado com sucesso!")

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder, ContextTypes, CommandHandler,
    CallbackQueryHandler
)

TOKEN = '7745042730:AAHFinhlcz2pnmK7TUbYT3Ndlw1aMpudlIM'  # ← Substitua pelo seu token real
LINK_GRUPO_OPERACOES = 'https://t.me/seu_grupo_aqui'
LINK_CADASTRO_CORRETORA = 'https://seu-link-da-corretora.com'

# Mensagem inicial
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    nome = update.effective_user.first_name or "investidor"

    mensagem = f"""
Fala {nome}. Teste01 aqui!

Agora você vai aprender a ganhar dinheiro junto comigo dentro do mercado financeiro. ✅

Para começar sua jornada comigo, siga esses passos 👇

✅ *Passo 01:* Entre no grupo de operações onde vou te enviar todas as entradas dentro do mercado financeiro para você copiar.

✅ *Passo 02:* Assista a aula fixada no grupo, para aprender a operar dentro do mercado.

✅ *Passo 03:* Faça seu cadastro na corretora e realize seu primeiro depósito para começar.

Pronto, depois disso você já pode ganhar dinheiro junto comigo 🔥
"""

    teclado = InlineKeyboardMarkup([
        [InlineKeyboardButton("🔒 Entrar no Grupo de Operações", url=LINK_GRUPO_OPERACOES)],
        [InlineKeyboardButton("📥 Cadastrar-se na Corretora", url=LINK_CADASTRO_CORRETORA)],
    ])

    await update.message.reply_text(
        mensagem,
        reply_markup=teclado,
        parse_mode="Markdown"
    )

# Função principal
def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    # Mantém o bot rodando
    print("Bot iniciado e aguardando comandos...")
    app.run_polling()

if __name__ == '__main__':
    main()

