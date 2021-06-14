import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import { RegisterPageComponent } from './register-page/register-page.component';
import { LoginPageComponent } from './login-page/login-page.component';
import { PageNotFoundComponent } from './page-not-found/page-not-found.component';
import { TodoListsPageComponent } from './todo-lists-page/todo-lists-page.component';

const routes: Routes = [
  {path:'register', component: RegisterPageComponent},
  {path:'login', component: LoginPageComponent},
  {path:'',component:TodoListsPageComponent},
  {path:'**', component: PageNotFoundComponent},
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
