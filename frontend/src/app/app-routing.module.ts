import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import { RegisterPageComponent } from './components/register-page/register-page.component';
import { LoginPageComponent } from './components/login-page/login-page.component';
import { PageNotFoundComponent } from './components/page-not-found/page-not-found.component';
import { TodoListsPageComponent } from './components/todo-lists-page/todo-lists-page.component';

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
